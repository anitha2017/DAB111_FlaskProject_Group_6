import pathlib
import sqlite3
import pandas as pd
from pathlib import Path
import csv

path = Path().cwd() # use pathlib to get current working directory


def create_db(db_name, filename, table_name):
    file_path =path / filename  # create a path to the data file

    con = sqlite3.connect(db_name) # create a connection to the database
    cursor = con.cursor() # create a cursor
    
    ford_dealers = pd.read_excel(file_path)
    # insert the data into the specified table 
    ford_dealers.to_sql(table_name, con, index=False, if_exists='replace')
    print(ford_dealers)

    # execute a select statement as f-string and print results to verify insertion
    results=cursor.execute(f"select *from {table_name}").fetchall()
    print(results)
    # commit the changes to the database
    con.commit()
    
    # close the connection
    con.close()
    


if __name__=="__main__":
    db_name = "dealers.db"
    filename = "../data_processing/ford_dealers.xlsx"
    table_name = "ford_dealers"
    create_db(db_name, filename, table_name)
