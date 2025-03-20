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
df