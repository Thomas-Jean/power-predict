import datetime

from fastapi import APIRouter
from backend.model_manager import ModelManager

router = APIRouter()

model_path = "src/model/dayton_power_model.pkl"

manager = ModelManager(model_path)

@router.get("/")
async def get_prediction():
	dates = [datetime.date.today(), datetime.date.today() + datetime.timedelta(days=1)]
	print('here')
	return manager.predict(dates)