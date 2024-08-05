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

def create_table(cursor):
   cursor.execute('''
   CREATE TABLE IF NOT EXISTS EmployeePerformance(
      id INT AUTO_INCREMENT PRIMARY KEY,
      employee_id INT,
      department VARCHAR(255),
      performance_score FLOAT,
      years_with_company INT,
      salary FLOAT
   )
   '''
   )
   print('EmployeePerformance table created/exists')

def run_program():
   conn = connect_to_mysql()
   if conn:
      cursor = conn.cursor()
      create_database(cursor)
      conn.database = 'CompanyData'
      create_table(cursor)

if __name__ == '__main__':
   run_program()