# power-predict

`fast-api` application that wraps around a simple `fbprophet` model and exposes an enpoint to query this model.

### env setup
you can setup an enviorment using `conda` and the provided `environment.yml`
```bash
conda env create -f environment.yml
```


### building the model
```bash
python model/build.py
```

one the model is built and pickled

### starting the application
```bash
uvicorn main:app
```

### tests
you can run unit tests with `pytest`