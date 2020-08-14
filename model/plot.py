import pandas as pd
import matplotlib.pyplot as plt
import pickle
from fbprophet import Prophet
from sklearn.metrics import mean_squared_error


df = pd.read_csv('./data/dayton_full.csv')


inital_data = df[:1095]
next_year = df[1095:1461]


pkl_path = "model/dayton_power_model.pkl"
with open(pkl_path, "rb") as file:
    model = pickle.load(file)

future = model.make_future_dataframe(periods=366, freq='D')

forecast = model.predict(future)
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())

y_pred = forecast[['yhat']][-366:].to_numpy()

y_true = next_year[['y']].to_numpy()

print(mean_squared_error(y_true, y_pred))

fig = model.plot(forecast)

print(next_year['ds'])
print(next_year['y'])
next_year['ds'] = pd.to_datetime(next_year['ds'])

fig.get_axes()[0].plot(next_year['ds'].dt.to_pydatetime(), next_year['y'], 'k.', zorder=1)
plt.show()

