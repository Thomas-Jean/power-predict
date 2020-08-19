FROM continuumio/miniconda3

WORKDIR app

COPY . .

RUN conda env create -f environment.yml

EXPOSE 8000

ENTRYPOINT ["conda", "run", "-n", "power", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]