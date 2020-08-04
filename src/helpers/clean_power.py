import pandas as pd


df = pd.read_csv('./data/dayton_hourly.csv')

print(df.head())

df['Datetime'] = pd.to_datetime(df['Datetime'])

sums = df.groupby(by=df['Datetime'].dt.date).sum().reset_index()

# sums = sums.sort_values(by=sums['Datetime'])

print(list(sums.columns.values))
print(sums.head())

sums.to_csv('./data/dayton_daily.csv', index=False)

