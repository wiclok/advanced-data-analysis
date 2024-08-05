import mysql.connector

def connect_to_mysql():
   try:
      conn = mysql.connector.connect(
         host="localhost",
         user="root",
         password=""
      )
      print("MySQL connection successful")
      return conn
   except mysql.connector.Error as err:
      print(f"Error connecting to MySQL: {err}")
      return None

def create_database(cursor):
   cursor.execute("CREATE DATABASE IF NOT EXISTS CompanyData")
   print('CompanyData database created/exists')
   
def run_program():
   conn = connect_to_mysql()
   if conn:
      cursor = conn.cursor()
      create_database(cursor)

if __name__ == '__main__':
   run_program()