import pandas as pd
import sqlite3

def load_csv(file):
    df = pd.read_csv(file)
    return df

def save_to_sql(df,table_name = "Uploaded_Data",db_path = "db/data.db"):
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name,conn,if_exists = "replace",index = False)
    conn.close

def get_sql_data(db_path = "db/data.db",table_name = "Uploaded_Data"):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql(f"SELECT * FROM {table_name}",conn)
    conn.close
    return df