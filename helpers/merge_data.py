import pandas as pd
from datetime import datetime


df_power = pd.read_csv('./data/dayton_daily.csv')

df_temp = pd.read_csv('./data/dayton_temp.csv')


df_power['Date'] = pd.to_datetime(df_power['Date'])

df_power = df_power[(df_power['Date'] >= datetime(year=2005,month=1,day=1)) & ( df_power['Date'] <= datetime(year=2017,month=12,day=31))].reset_index(drop=False)


df_temp['Date'] = pd.to_datetime(df_temp['Date'])

df_temp = df_temp[(df_temp['Date'] >= datetime(year=2005,month=1,day=1)) & ( df_temp['Date'] <= datetime(year=2017,month=12,day=31))].reset_index(drop=False)


df_full = df_temp.merge(df_power, on='Date')[['Date', 'Temp', 'DAYTON_MW']]

df_full = df_full.rename(columns={ 'DAYTON_MW': 'y', 'Date': 'ds', 'Temp': 't'})


df_full.to_csv('./data/dayton_full.csv', index=False)
