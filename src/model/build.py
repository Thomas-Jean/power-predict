import pandas as pd
import matplotlib.pyplot as plt
import pickle
from fbprophet import Prophet
from sklearn.metrics import mean_squared_error


df = pd.read_csv('./data/dayton_full.csv')


inital_data = df[:1095]

model = Prophet()
model.fit(inital_data)

pkl_path = "src/model/dayton_power_model.pkl"
with open(pkl_path, "wb") as file:
    pickle.dump(model, file)