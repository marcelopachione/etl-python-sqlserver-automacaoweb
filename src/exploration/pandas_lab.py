## Convert data pandas

#%%
import pandas as pd
import os

df = pd.read_csv(r'../datasets/csv/Clientes.csv', delimiter=',')

df['number'] = df['number'].astype('str')
df['created_at'] = pd.to_datetime(df['created_at'])


for col in df.columns:
    print(f"Column: {col}, Data type: {df[col].dtype}")


df.head()

#%%
# Filter data

df_filteres = df[(df['created_at'].dt.year >= 2018) & (df['created_at'].dt.year <= 2021)]
df_filteres

df_filteres = df[(df['created_at'].dt.year == 2018) | (df['created_at'].dt.year == 2021)]
df_filteres

#%%
# Convert to br model
#%%
import pandas as pd
import os

df = pd.read_csv(r'../datasets/csv/Clientes.csv', delimiter=',')

# Converte coluna created_at para datatime br
df['created_at'] = pd.to_datetime(df['created_at']).dt.strftime('%d/%m/%Y %H:%M:%S') 
df.head()

#%% 
## Add columns pandas --> full_name
import pandas as pd
import os

df = pd.read_csv(r'../datasets/csv/Clientes.csv', delimiter=',')

df['full_name'] = df['first_name'] + ' ' + df['last_name']
df.head()

#%%
## Separa a data em colunas --> (year, month, day)
import pandas as pd
import os

months = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

df = pd.read_csv(r'../datasets/csv/Clientes.csv', delimiter=',')
df['year'] = pd.to_datetime(df['created_at']).dt.year
df['month'] = pd.to_datetime(df['created_at']).dt.month
df['day'] = pd.to_datetime(df['created_at']).dt.day
df['desc_month'] = df['month'].apply(lambda x: months[x-1])

df.head()

#%% 
# Trabalhando com excel que possuem outras abas
import pandas as pd
import os

df = pd.read_excel(r'../datasets/excel/Caquinha.xlsx')
display(df)

#%%
import pandas as pd
import os

df = pd.read_excel(r'../datasets/excel/Caquinha.xlsx', sheet_name='Planilha2')
display(df)

#%%
import pandas as pd
import os

df = pd.read_excel(r'../datasets/excel/Caquinha.xlsx', sheet_name='Planilha2', skiprows=3)
display(df)

#%%
import pandas as pd
import os

df = pd.read_excel(r'../datasets/excel/Caquinha.xlsx', sheet_name='Planilha3', usecols='A:B')
display(df)

#%%
import pandas as pd
import os

df = pd.read_excel(r'../datasets/excel/Caquinha.xlsx', sheet_name='Planilha5', nrows=11)
display(df)

#%%
# Selecionando colunas
import pandas as pd
import os

df = pd.read_csv(r'../datasets/csv/Clientes.csv', delimiter=',')
dfcols = df[['id', 'first_name', 'last_name', 'email', 'created_at']]
display(dfcols)

#%%
# Verifica se há valores duplicados
import pandas as pd
import os

df = pd.read_excel(r'../datasets/excel/Vendas2021.xlsx')
df.duplicated('Categoria') 

#%%
# Remove valores duplicados
import pandas as pd
import os

df = pd.read_excel(r'../datasets/excel/Vendas2021.xlsx')

duplicated = df[df.duplicated('Categoria')]
df_without_duplicated = df.drop_duplicates(subset='Categoria', keep='first')    

# orderna o dataframe, e aplicando no dataframe
df_without_duplicated.sort_values(by='IdPais', ascending=True, inplace=True)

# Renomeia as colunas
df_without_duplicated = df_without_duplicated.rename(columns={'Vendas total' : 'VendasTotal'})
df_without_duplicated