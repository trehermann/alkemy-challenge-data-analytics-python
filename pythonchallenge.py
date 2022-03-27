import datetime
import os
import pandas
import re
import requests
from decouple import config
from skimpy import clean_columns
from sqlalchemy import create_engine

museumdata_url = config('MUSEUMS_URL')
cinemadata_url = config('CINEMAS_URL')
librariesdata_url = config('LIBRARIES_URL')

currentdate = datetime.datetime.now() 

museumdata_folder = (
    'museums' + '/'
    + currentdate.strftime('%Y-%B') + '/'
)

museumdata_csvpath = (
	'museums-' + currentdate.strftime('%d-%m-%Y') + '.csv'
)

museumdata_fullpath = os.path.join(museumdata_folder, museumdata_csvpath)


os.makedirs(museumdata_folder, exist_ok=True) # overwrite folder if it exists

# os.makedirs('museums' + '/' + currentdate.strftime('%Y-%B'))
museumdata_csv = open(museumdata_fullpath, 'wb')
museumdata_csv.write(requests.get(museumdata_url).content)
museumdata_csv.close

dirty_df = pandas.read_csv(museumdata_fullpath)
final_df_columns = [
    'cod_loc',
    'id_provincia',
    'id_departamento',
    'categoria',
    'provincia',
    'localidad',
    'nombre',
    'direccion',
    'cp',
    'telefono',
    'mail',
    'web'
]


# dataframe column names, from camelcase to snakecase
df = clean_columns(dirty_df)
df = df.drop(columns=[
    col for col in df 
    if col not in final_df_columns
])

print(df.columns.tolist())

