import psycopg2
import os
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Access the variables

database_url = os.getenv("DATABASE_URL")


# Connect to PostgreSQL database
conn = psycopg2.connect(database_url)

# Create a cursor object
cursor = conn.cursor()

# Get all table names from the current schema
cursor.execute("""
    SELECT table_name 
    FROM information_schema.tables 
    WHERE table_schema = 'public'
""")
tables = cursor.fetchall()

# Create a dictionary to hold the data from each table
table_data = {}

# Loop through each table and load the data into a variable (as a pandas DataFrame)
for table in tables:
    table_name = table[0]
    query = f"SELECT * FROM {table_name}"
    table_df = pd.read_sql(query, conn)
    
    # Store each table's data as a DataFrame in the dictionary, with the table name as the key
    table_data[table_name] = table_df

# Close the connection
cursor.close()
conn.close()

# Access data of each table from `table_data` dictionary
# Example: To access the 'student_table' data
student_data = table_data['student_table']
attendance_table = table_data['attendance_table']
class_resources_table = table_data['class_resources_table']
extracurricular_activity = table_data['extracurricular_activity']
parent_table = table_data['parent_table']
ss3_student_survey = table_data['ss3_student_survey']
staff_table = table_data['staff_table']
student_performance = table_data['student_performance']
teachers_table = table_data['teachers_table']

