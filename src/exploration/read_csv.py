# Working with csv
#%%
import pandas as pd

#%%
# Read csv file
df = pd.read_csv(r"../datasets/csv/Clientes.csv", delimiter = ',')
df.head()

#%%
# Find itens state == 'Mato Grosso'
df_state = df.loc[df['state'] == 'Mato Grosso']
df_state

#%%
# Filter states
df_states = df.loc[df['state'].isin(['Rio de Jaineiro', 'Bahia', 'Rio Grande do Sul'])]
df_states

#%%
# Working with null's

# Replace Null Values
df['street'] = df['street'].fillna('Not found')
df['number'] = df['number'].fillna('No number')
df['additionals'] = df['additionals'].fillna('No info')
df['email'] = df['email'].fillna('Not registered')
df

#%%
# Replace Method

# Read csv file
df2 = pd.read_csv(r"../datasets/csv/Clientes.csv", delimiter = ',')
df2.head()

df2['street'] = df2['street'].fillna('Not found')
df2['number'] = df2['number'].fillna('No number')
df2['additionals'] = df2['additionals'].fillna('No info')
df2['email'] = df2['email'].fillna('Not registered')
df2['state'] = df2['state'].fillna('Not found')
df2

#%%
# Change specif value
old_values = 'São Paulo'
new_values = 'SP'

df2['state'] = df['state'].replace(old_values, new_values)
df2

#%%
# CHange a list of values
mapping = {
'Acre' : 'AC',
'Alagoas' : 'AL',
'Amapá' : 'AP',
'Amazonas' : 'AM',
'Bahia' : 'BA',
'Ceará' : 'CE',
'Brasília' : 'DF',
'Espírito Santo' : 'ES',
'Goiás' : 'GO',
'Maranhão' : 'MA',
'Mato Grosso' : 'MT',
'Mato Grosso do Sul' : 'MS',
'Minas Gerais' : 'MG',
'Pará' : 'PA',
'Paraíba' : 'PB',
'Paraná' : 'PR',
'Pernambuco' : 'PE',
'Piauí' : 'PI',
'Rio de Janeiro' : 'RJ',
'Rio Grande do Norte' : 'RN',
'Rio Grande do Sul' : 'RS',
'Rondônia' : 'RO',
'Roraima' : 'RR',
'Santa Catarina' : 'SC',
'São Paulo' : 'SP',
'Sergipe' : 'SE',
'Tocantins' : 'TO',
}

df2['state'] = df2['state'].replace(mapping)
df2