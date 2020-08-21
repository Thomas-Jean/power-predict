import pytest
import fbprophet
from datetime import date
from . import model_manager


def test_load_model():
    model_path = "model/dayton_power_model.pkl"

    mm = model_manager.ModelManager(model_path)
    assert type(mm.model) is fbprophet.forecaster.Prophet


def test_model_predict():
    model_path = "model/dayton_power_model.pkl"

    test_date = [date(2020,1,1)]

    mm = model_manager.ModelManager(model_path)
    results = mm.predict(test_date)


    assert results[0]['date'] == date(2020,1,1)
    assert isinstance(results[0]['mw'], float)