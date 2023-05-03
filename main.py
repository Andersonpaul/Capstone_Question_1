from etl import read_data,download_data
from util import load_data

download_data()
covid_df = read_data()
load_data(covid_df)