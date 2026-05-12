import mysql.connector as myc 
from mysql.connector import pooling
from dotenv import load_dotenv
import os
load_dotenv()

host=os.getenv("host_db")
user=os.getenv("user_db")
pass_w=os.getenv("pass_db")
db=os.getenv("db_name")

dbconfig = {
    "host": host,
    "user": user,
    "password": pass_w,
    "database": db
}


class Some_delete_function():
    def __init__(self):
        self.cursor,self.conn = get_cursore()
        
    def create_table(self):
        cursor = self.cursor
        conn = self.conn
        cursor.execute(
            """CREATE TABLE leads (
            id INT AUTO_INCREMENT PRIMARY KEY,
            country VARCHAR(100),
            business VARCHAR(255),
            query TEXT,
            is_used BOOLEAN DEFAULT FALSE)"""
        )
        conn.commit()
        
    def create_table_get_lead(self):
        cursor = self.cursor
        conn = self.conn
        query = """
                    CREATE TABLE LEAD_GET_GOOGLE_MAP (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    query_id INT,
                    business_name VARCHAR(100) NOT NULL,
                    link VARCHAR(300) NOT NULL,

                    FOREIGN KEY (query_id)
                        REFERENCES leads(id)
                );
                """
        cursor.execute(query)
        conn.commit()
    
    def delete_all_dummy_data_from_google_map_table(self):
        cursor = self.cursor
        conn = self.conn
        query = "TRUNCATE TABLE LEAD_GET_GOOGLE_MAP"
        cursor.execute(query)
        print("delete all data in table")
        conn.commit()
        return

    def reset_all_is_used(self):
        cursor = self.cursor
        conn = self.conn
        try:
            cursor.execute(
                "UPDATE leads SET is_used = FALSE"
            )
            conn.commit()
            print("All leads reset: is_used = FALSE ✅")

        except Exception as e:
            print("Reset failed:", e)
            conn.rollback()
    def close(self):
        self.cursor.close()
        self.conn.close()

pool = pooling.MySQLConnectionPool(
    pool_name="mypool",
    pool_size=5,
    pool_reset_session=True,
    **dbconfig
)

def get_cursore():
    conn = pool.get_connection()   # 👈 bas yahi change
    cursor = conn.cursor()
    return cursor, conn 

if __name__ == "__main__":
    # create_table()
    obj = Some_delete_function()
    obj.delete_all_dummy_data_from_google_map_table()
    obj.reset_all_is_used()
    obj.close()