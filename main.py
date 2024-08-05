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

def run_program():
   conn = connect_to_mysql()

if __name__ == '__main__':
   run_program()