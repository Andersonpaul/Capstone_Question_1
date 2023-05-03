import pandas as pd
import os
from dotenv import load_dotenv,dotenv_values
import requests
from bs4 import BeautifulSoup as bs
import opendatasets as od
from datetime import datetime


def download_data():
   sheet_url = 'https://drive.google.com/file/d/1SzmRIwlpL5PrFuaUe_1TAcMV0HYHMD_b/view'
   od.download_google_drive(sheet_url,'./')

def read_data():
   covid_dataframe = pd.read_csv('covid_19_data.csv')
   covid_dataframe.columns=['sno','observationdate','province','country','lastupdate','confirmed','deaths','recovered']
   covid_dataframe['observationdate'] = pd.to_datetime(covid_dataframe['observationdate'])
   print(covid_dataframe.head(5))
   return covid_dataframe






