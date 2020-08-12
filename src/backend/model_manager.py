import pickle
import pandas as pd
from fbprophet import Prophet


class ModelManager(object):

	def __init__(self, model_path):
		with open(model_path, "rb") as file:
		    self.model = pickle.load(file)

	@staticmethod
	def map_prediction(df):
		predictions = []
		for row in df.itertuples():
			predictions.append({'date': row.ds, 'mw': row.yhat})

		return predictions


	def predict(self, dates):
		predictions = self.model.predict(pd.DataFrame(data={'ds': dates }))

		return ModelManager.map_prediction(predictions)
