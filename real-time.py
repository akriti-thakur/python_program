import datetime
import time
import random
import mysql.connector
from mysql.connector import Error

# Establish the connection
try:
    con = mysql.connector.connect(
        host='localhost',
        user='root',  # Corrected from 'username' to 'user'
        password='1234',
        database='data'
    )

    if con.is_connected():
        print("Connection successfully created")
        my_cursor = con.cursor()

except Error as e:
    print(f"Error: {e}")

def data():
    while True:
        date = datetime.date.today().strftime('%Y-%m-%d')  # Ensure date is in 'YYYY-MM-DD' format
        location_id = random.randint(111, 201)
        company = random.randint(11, 30)
        issue_id = random.randint(111, 130)
        csr_id = random.randint(111, 210)
        response_time = random.randint(1, 300)
        call_time = random.randint(1, 600)
        status = random.randint(1, 100)
        if status <75:
            status=1
        elif status <85:
            status=2
            
        elif status<90:
            status=3
            
        else:
            status=4
        
        if status == 1:
            rating = random.randint(5, 10)
        elif status == 2:
            rating = random.randint(3, 8)
        elif status == 3:
            rating = random.randint(1, 3)
        elif status == 4:
            rating = random.randint(1, 5)
        
        # Insert data into MySQL table
        sql = """
        INSERT INTO call_data (date, location_id, company, issue_id, csr_id, response_time, call_time, status, rating)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        val = (date, location_id, company, issue_id, csr_id, response_time, call_time, status, rating)
        my_cursor.execute(sql, val)
        con.commit()
        
        print(date, location_id, company, issue_id, csr_id, response_time, call_time, status, rating)
        print("----------------------------")
        time.sleep(5)

if __name__ == "__main__":
    data()

    # Close the cursor and connection when done
    my_cursor.close()
    con.close()
