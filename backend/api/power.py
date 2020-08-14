import datetime
import pandas as pd
from typing import Optional

from fastapi import APIRouter, Query
from backend.model_manager import ModelManager

router = APIRouter()

model_path = "model/dayton_power_model.pkl"

manager = ModelManager(model_path)

@router.get("/")
async def get_prediction(start_date: datetime.date = Query(datetime.date.today()), end_date: Optional[datetime.date] = Query(None)):
	dates = []

	if(end_date is None or end_date < start_date):
		dates = [start_date]
	else:
		dates = pd.date_range(start=start_date, end=end_date).to_list()

	return manager.predict(dates)