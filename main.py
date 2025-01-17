import mysql.connector
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def connect_to_mysql():
   try:
      conn = mysql.connector.connect(
         host="tu_host",
         user="tu_usuario",
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
      host='tu_host',
      user='tu_usuario',
      password='',
      database="CompanyData"
   )
   query = 'SELECT * FROM EmployeePerformance'
   df = pd.read_sql(query, conn)
   conn.close()
   return df

def analize_data(df):

   statistics = df.groupby('department').agg({
   'performance_score': ['mean', 'median', 'std'],
   'salary': ['mean', 'median', 'std'],
   'employee_id': 'count'
   }).rename(columns={'employee_id': 'total_employees'})
   
   correlation_years_performance = df[['years_with_company', 'performance_score']].corr().iloc[0, 1]
   correlation_salary_performance = df[['salary', 'performance_score']].corr().iloc[0, 1]
   
   return statistics, correlation_years_performance, correlation_salary_performance

def vizualize_data(df):
   departments = df['department'].unique()
   for department in departments:
      plt.figure()
      df[df['department'] == department]['performance_score'].hist()
      plt.title(f'Histograma de performance_score para {department}')
      plt.xlabel('performance_score')
      plt.ylabel('Frecuencia')
      plt.show()

   plt.figure()
   plt.scatter(df['years_with_company'], df['performance_score'])
   plt.title('Años en la empresa vs. Puntuación de rendimiento')
   plt.xlabel('Años en la empresa')
   plt.ylabel('Puntuación de rendimiento')
   plt.show()

   plt.figure()
   plt.scatter(df['salary'], df['performance_score'])
   plt.title('Salario vs. Puntuación de rendimiento')
   plt.xlabel('Salario')
   plt.ylabel('Puntuación de rendimiento')
   plt.show()

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
      statics, correlation_years_performance, correlation_salary_performance = analize_data(df)
      print(statics)
      print(f"correlation_years_performance {correlation_years_performance}")
      print(f"correlation_salary_performance {correlation_salary_performance}")
      vizualize_data(df)

if __name__ == '__main__':
   run_program()