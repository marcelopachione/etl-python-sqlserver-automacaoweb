## Trabalhando com SQL Server

#%%
# Importando bibliotecas
import pandas as pd
import pyodbc
import os

server = 'localhost'
database = 'PythonDB'
username = 'sa'
password = 'Fiduma@01'

connDB = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'  
    f'SERVER={server};' 
    f'DATABASE={database};' 
    f'UID={username};'
    f'PWD={password};'
    f'Trusted_Connection=no;'
    )

#%%
# Carrega dataframe
df = pd.read_csv(r'../datasets/csv/Clientes.csv', delimiter=',')
df = df[['first_name', 'last_name', 'email', 'created_at']]
df['email'] = df['email'].fillna('Sem email')

# Insere dataframe no banco de dados
cursor = connDB.cursor()

for index, row in df.iterrows():
    cursor.execute("INSERT INTO [clientes_tmp] (first_name, last_name, email, created_at) values(?,?,?,?)", row['first_name'], row['last_name'], row['email'], row['created_at'])
    connDB.commit()
    cursor.close()
    connDB.close()