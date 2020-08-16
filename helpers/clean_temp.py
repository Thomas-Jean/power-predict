import pandas as pd
from datetime import date


df = pd.read_csv('./data/city_temperature.csv')


df = df[df["City"] == "Dayton"]

print(df.head())

df['Date'] = df.apply(lambda row: date(row['Year'], row['Month'], row['Day']), axis=1)



results = df[['Date', 'AvgTemperature']]

results = results.rename(columns={ 'AvgTemperature': 'Temp'})


print(results.head())

results.to_csv('./data/dayton_temp.csv', index=False)
