#%%
import pandas as pd

#%%
# Load df
df = pd.read_excel(r"../datasets/excel/Produto.xlsx")
df.head()
df

#%%
# Find first item == "Calça"
df_calca = df.loc[df['Name'] == 'Calça']
df_calca

#%%
# Find a list of products
itens = ['Shampoo', 'Perfume', 'Protetor Solar', 'Sapato vermelho']
df_itens = df.loc[df['Name'].isin(itens)]
df_itens

#%%
# Find products price > 1000
df_mais_1000 = df.loc[df['Price'] > 1000]
df_mais_1000

#%%
df200a1000 = df.loc[(df['Price'] >= 200) & (df['Price'] <= 1000)]
df200a1000.head(10)