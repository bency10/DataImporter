import psycopg2
from psycopg2.extras import Json
from data_importer.logger import logger

class Database:
    def __init__(self, config):
        self.conn = psycopg2.connect(
            host=config['host'],
            port=config['port'],
            user=config['user'],
            password=config['password'],
            dbname=config['dbname']
        )
        self.cursor = self.conn.cursor()

    def create_table(self):
        try:
            create_table_query = """
            CREATE TABLE IF NOT EXISTS public.phone (
                phoneid text PRIMARY KEY,
                phone_name text,
                phone_data jsonb
            );
            """
            self.cursor.execute(create_table_query)
            self.conn.commit()
        except Exception as e:
            logger.error(f"Error creating table: {e}")

    def insert_phone_data(self, phone_id, phone_name, phone_data):
        try:
            insert_query = """
            INSERT INTO public.phone (phoneid, phone_name, phone_data)
            VALUES (%s, %s, %s)
            ON CONFLICT (phoneid) DO NOTHING;
            """
            self.cursor.execute(insert_query, (phone_id, phone_name, Json(phone_data)))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Error inserting data into database: {e}")
