import pandas as pd
import mysql.connector
from mysql.connector import Error

def connect_to_mysql():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1234',
            database='blinkit_data',
            ssl_disabled=True,
            connection_timeout=60,
            autocommit=True
        )
        if conn.is_connected():
            print("MySQL connection established")
            return conn
    except Error as e:
        print(f"Connection Error: {e}")
        return None

def bulk_insert(df_chunk, table_name, cursor, conn):
    columns = ', '.join(df_chunk.columns)
    placeholders = ', '.join(['%s'] * len(df_chunk.columns))
    insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    
    data = [tuple(row) for row in df_chunk.to_numpy()]
    try:
        cursor.executemany(insert_query, data)
        conn.commit()
        print(f"Inserted {len(data)} rows into {table_name}")
    except Error as e:
        print(f" Failed to insert into {table_name}: {e}")

#  Main execution with chunking
conn = connect_to_mysql()
if conn:
    cursor = conn.cursor()

    csv_path = 'C:/Users/akrit/Downloads/all_blinkit_category_scraping_streams.csv' 
    chunksize = 50000  

    try:
        for i, chunk in enumerate(pd.read_csv(csv_path, chunksize=chunksize)):
            print(f"Processing chunk {i+1}")
            bulk_insert(chunk, 'all_blinkit_category_scraping_stream', cursor, conn)
    except Exception as e:
        print(f"Error reading or inserting CSV: {e}")

    cursor.close()
    conn.close()
    print("MySQL connection closed.")
