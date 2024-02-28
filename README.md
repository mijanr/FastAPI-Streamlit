

## Streamlit Multi-Page Functionality
The following links were used to implement the multi-page functionality in streamlit:
 - https://docs.streamlit.io/get-started/tutorials/create-a-multipage-app
 - https://docs.streamlit.io/library/advanced-features/multipage-apps


## Run Streamlit App
To run the streamlit app, first FastAPI app should be running. To run the FastAPI app, run the following command:

```
uvicorn main:app --reload
```
Once the FastAPI app is running, run the following command to run the streamlit app:
```
streamlit run app/Home.py
```

## Requirements
requirements.yml file contains the list of all the packages required to run the code in this repository. requirements.yml is generated using the following command:

```
conda env export --no-builds | grep -v "prefix" > requirements.yml
```
To create a conda environment using the requirements.yml file, run the following command:

```
conda env create -f requirements.yml
```