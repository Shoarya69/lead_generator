from app.connect_mysql_for_123 import get_cursore as gc
import pandas as pd

df = pd.read_csv("/home/shoarya/Desktop/leadomator/app/data/lead_comb_main_main.csv")

def data_pipline_form_csv_to_sql():
    cursor,conn = gc()
    data =  df[["Country","Business","query",'tier']].values.tolist()
    cursor.executemany(
        "INSERT INTO leads (country, business, query,tier) VALUES (%s, %s, %s,%s)",
        data
    )
    conn.commit()
    print("success")

if __name__ == "__main__":
    data_pipline_form_csv_to_sql()