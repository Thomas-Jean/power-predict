import pandas as pd
import pickle
import datetime

from fastapi import FastAPI
from fbprophet import Prophet

app = FastAPI()

pkl_path = "src/model/dayton_power_model.pkl"
with open(pkl_path, "rb") as file:
    model = pickle.load(file)


def map_prediction(df):
	predictions = []
	for row in df.itertuples():
		predictions.append({'date': row.ds, 'mw': row.yhat})

	return predictions

@app.get("/")
async def root():

    return map_prediction(model.predict(pd.DataFrame(data={'ds': [datetime.date.today(), datetime.date.today() + datetime.timedelta(days=1)]})))

