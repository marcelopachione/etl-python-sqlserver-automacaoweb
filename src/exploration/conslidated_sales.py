# Consolidating sales

#%%
import pandas as pd 
import os

#%%
sales2021 = pd.read_excel(r"../datasets/excel/Vendas2021.xlsx")
sales2022 = pd.read_excel(r"../datasets/excel/Vendas2022.xlsx")
sales2023 = pd.read_excel(r"../datasets/excel/Vendas2023.xlsx")

sales2021.head()
sales2022.head()
sales2023.head()

#%%
## Consolidating sales
import pandas as pd
import os

# Dest path
sales_dir = (r'../datasets/excel')

sales_data = []

for file in os.listdir(sales_dir):
    if file.endswith('.xlsx') and 'vendas' in file.lower():
        file_path = os.path.join(sales_dir, file)
        df = pd.read_excel(file_path)
        sales_data.append(df)

conslidated_sales = pd.concat(sales_data)
conslidated_sales.head()


#%% 
# Save the consolidated data - excel
dest_dir = (r'../datasets/excel/conslidated_sales')
excel_file = 'tabajara_sales.xlsx'
full_dest_path = os.path.join(dest_dir, excel_file)

# Remove the file if it already exists
if os.path.exists(full_dest_path):
    os.remove(full_dest_path)

conslidated_sales.to_excel(full_dest_path, index = False)

#%% 
# Save the consolidated data - csv
dest_dir = (r'../datasets/excel/conslidated_sales')
csv_file = 'tabajara_sales.csv'
full_dest_path = os.path.join(dest_dir, csv_file)

# Remove the file if it already exists
if os.path.exists(full_dest_path):
    os.remove(full_dest_path)

conslidated_sales.to_csv(full_dest_path, sep=',',  index = False)

#%% 
# Save the consolidated data - json
dest_dir = (r'../datasets/excel/conslidated_sales')
json_file = 'tabajara_sales.json'
full_dest_path = os.path.join(dest_dir, json_file)

# Remove the file if it already exists
if os.path.exists(full_dest_path):
    os.remove(full_dest_path)

conslidated_sales.to_json(full_dest_path, orient = 'records', indent=4)





###############ip install --upgrade pip###############################################################
### Testes Minio / boto3
##############################################################################
#%%
########################################################
# Save the consolidated data to datalake - excel
########################################################
import pandas as pd
from minio import Minio
from minio.error import S3Error
import os

# Bucket name
bucket_name = 'raw'
# Directory containing Excel sales files
sales_dir = r'../datasets/excel'

# Minio client configuration
client = Minio(
    'localhost:9000',
    #'192.168.56.101:9000',
    access_key='minio',
    secret_key='minio@123',
    secure=False
)


if not client.bucket_exists(bucket_name):
    client.make_bucket(bucket_name)

try:
    for file_name in os.listdir(sales_dir):
        if file_name.endswith('.xlsx') and 'vendas20' in file_name.lower():
            file_path = os.path.join(sales_dir, file_name)
            client.fput_object(bucket_name, file_name, file_path)
            print(f'File {file_name} uploaded to {bucket_name}/{file_name}')
except S3Error as err:
    print(f'Error occurred: {err}')
except Exception as e:
    print(f'Unexpected error: {e}')


#%% 
# Using boto3
import boto3

s3 = boto3.client('s3',
                  endpoint_url='http://localhost:9000',
                  aws_access_key_id='minio',
                  aws_secret_access_key='minio@123')

res = s3.list_objects(Bucket='raw')
for obj in res.get('Contents', []):
    print(obj['Key'])