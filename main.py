import mysql.connector
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

def read_csv(filename):
   with open(filename, 'r') as archive:
      reader = csv.reader(archive, delimiter=',', quotechar='"')
      Headboard = next(reader)
      employees = []
      for row in reader:
         employees.append(tuple(row))
      return Headboard, employees

def insert_data(cursor, employees):
   # Verificar si la tabla está vacía
   cursor.execute('SELECT COUNT(*) FROM EmployeePerformance')
   count = cursor.fetchone()[0]

   if count == 0:
      insert_data_query = 'INSERT INTO EmployeePerformance (employee_id, department, performance_score, years_with_company, salary) VALUES (%s, %s, %s, %s, %s)'
      for employee in employees:
         cursor.execute(insert_data_query, employee[1:])
      cursor._connection.commit()
      cursor.close()
      print("Registros insertados con éxito.")
   else:
      print("La tabla ya contiene datos. No se insertaron nuevos registros.")

def extract_data():
   conn = mysql.connector.connect(
      host='localhost',
      user='root',
      password='',
      database="CompanyData"
   )
   query = 'SELECT * FROM EmployeePerformance'
   df = pd.read_sql(query, conn)
   conn.close()
   return df

def run_program():
   conn = connect_to_mysql()
   if conn:
      cursor = conn.cursor()
      create_database(cursor)
      conn.database = 'CompanyData'
      create_table(cursor)
      filename = 'MOCK_DATA.csv'
      headboard, employees = read_csv(filename)
      insert_data(cursor, employees)
      df = extract_data()

if __name__ == '__main__':
   run_program()