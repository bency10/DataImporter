import yaml
from data_importer.api_client import APIClient
from data_importer.db import Database
from data_importer.logger import logger

def load_config():
    with open('config/config.yaml', 'r') as file:
        return yaml.safe_load(file)

def main():
    config = load_config()
    api_client = APIClient(config['api']['url'])
    db = Database(config['database'])
    
    logger.info("Creating database table...")
    db.create_table()

    logger.info("Fetching data from API...")
    mobile_data = api_client.fetch_mobile_data()

    logger.info("Inserting data into database...")
    for item in mobile_data:
        db.insert_phone_data(item['id'], item['name'], item.get('data', {}))

    logger.info("Data import completed successfully.")

if __name__ == "__main__":
    main()
