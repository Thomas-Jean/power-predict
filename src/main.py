import pandas as pd
import matplotlib.pyplot as plt
from fbprophet import Prophet


df = pd.read_csv('./example_air_passengers.csv')
print(df.head())


m = Prophet()
m.fit(df)

future = m.make_future_dataframe(periods=36, freq='M')

forecast = m.predict(future)
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())

fig = m.plot(forecast)

plt.show()