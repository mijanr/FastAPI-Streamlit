from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/iris")
def get_iris_dataset():
    
    # load the iris dataset
    iris = pd.read_csv('data/iris.csv')
    
    return iris.to_dict(orient="records")

