import datetime
import os
import pandas
import requests
from decouple import config
from skimpy import clean_columns

currentdate = datetime.datetime.now()

data = [
    'museums',
    'cinemas',
    'libraries'
]


for i in data:
    global data_path 
    data_path = i + '/' + currentdate.strftime('%Y-%B') + '/'
    global data_fullpath
    data_fullpath = os.path.join(
        data_path, 
        i + '-' + currentdate.strftime('%d-%m-%Y') + '.csv')    
    global final_df_columns 
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
        
    os.makedirs(
        data_path,
        exist_ok=True
    )

    data_csv = open(data_fullpath, 'wb')
    data_csv.write(requests.get(config(i.upper() + '_URL')).content )
    data_csv.close   
    
    dirty_df = pandas.read_csv(data_fullpath)
    df = clean_columns(dirty_df)
    df = df.drop(
        columns = [
            col for col in df
            if col not in final_df_columns
            ]
        )
    print(df.columns.tolist())
  