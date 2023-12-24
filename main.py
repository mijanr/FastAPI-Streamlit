from fastapi import FastAPI
import seaborn as sns

app = FastAPI()

@app.get("/iris")
def get_iris_data():
    iris = sns.load_dataset("iris")
    return iris
