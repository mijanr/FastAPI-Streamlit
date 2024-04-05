# src/app.py
import streamlit as st
import pandas as pd
# welcome message
st.title("Iris dataset explorer")
st.write(
    "This is a simple multi-page Iris dataset explorer app. \
     It uses a ```FastAPI``` backend to serve the ```Iris``` dataset EDA and \
     make predictions using a pre-trained model. \
     The frontend is built using Streamlit.")

