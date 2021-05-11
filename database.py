import MySQLdb
import pandas
from pandas.io import sql
from sqlalchemy import create_engine

conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="", db="Python_app")

def search_database(name):
    conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="", db="Python_app")
    cur = conn.cursor()
    cur.execute("SELECT title,price FROM jumia_data WHERE title LIKE %s " , ("%" + name + '%',))
    result = cur.fetchall()
    for row in result:
        print(str(row[0:2]).replace("(", " " ).replace(")"," ").replace("'"," "),'\n')
    cur.close()


def insert_to_sql():
    conn = create_engine('mysql://root:''@localhost/python_app')
    df = pandas.read_csv("C:/Users/Wambugu/Jumia_data.csv",usecols=['Title','Price'],encoding='utf-8')
    with conn.connect() as con ,con.begin():
        df.to_sql(con=con,name='jumia_data',if_exists='append',index=False)
    print("DOOOONE")

x = input("ENTER NAME: ")
search_database(x)



