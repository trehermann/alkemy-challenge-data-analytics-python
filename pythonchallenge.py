import datetime
import os
import requests
from decouple import config
from sqlalchemy import create_engine

currentdate = datetime.datetime.now()
museumdata_url = config('MUSEUMS_URL')
cinemadata_url = config('CINEMAS_URL')
librariesdata_url = config('LIBRARIES_URL')
museumdata_path = (
    'museums' + '/'
    + currentdate.strftime('%Y-%B') + '/'
    + 'museums-' + currentdate.strftime('%d-%m-%Y') + '.csv'
)


# os.makedirs('museums' + '/' + currentdate.strftime('%Y-%B'))

museumdata_csv = open(museumdata_path, 'wb')
museumdata_csv.write(requests.get(museumdata_url).content)
museumdata_csv.close

