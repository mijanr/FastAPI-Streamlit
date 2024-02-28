from fastapi import FastAPI
import pandas as pd
import joblib
from typing import List
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/app", StaticFiles(directory="app", html=True), name="app")


# get the iris dataset
@app.get("/iris")
def get_iris_dataset():
    
    # load the iris dataset
    iris = pd.read_csv('data/iris.csv')
    
    return iris.to_dict(orient="records")

# load the pre-trained model
model = joblib.load("saved_model/saved_model.joblib")

# define the input data model
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# define the prediction endpoint
@app.post("/predict", response_model=List[float])
async def predict(data: IrisInput):
    input_data = [[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]]
    prediction = model.predict(input_data)
    pred_prob = model.predict_proba(input_data)
    
    return prediction, pred_prob.max()*100