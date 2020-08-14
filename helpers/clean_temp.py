import pandas as pd
from datetime import date


df = pd.read_csv('./data/dayton_temp_raw.csv')

print(df.head())


df['Date'] = df.apply(lambda row: date(row['Year'], row['Month'], row['Day']), axis=1)



results = df[['Date', 'Temp']]

print(results.head())

results.to_csv('./data/dayton_temp.csv', index=False)
