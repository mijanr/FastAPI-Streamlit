

## Streamlit Multi-Page Functionality
The following links were used to implement the multi-page functionality in streamlit:
 - https://docs.streamlit.io/get-started/tutorials/create-a-multipage-app
 - https://docs.streamlit.io/library/advanced-features/multipage-apps


## Run Streamlit App
To run the streamlit app, run the following command:

```
streamlit run src/app.py
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