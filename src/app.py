# src/app.py
import streamlit as st
import pandas as pd
from fastapi import HTTPException

# Load the Iris dataset
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", header=None)
        df.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
        return df
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading data: {str(e)}")

df = load_data()

# Streamlit app
def main():
    st.title("Iris Dataset EDA")

    # Create buttons in the sidebar for each page
    raw_data_button = st.sidebar.button("Raw Data")
    summary_stats_button = st.sidebar.button("Summary Statistics")
    class_distribution_button = st.sidebar.button("Class Distribution")

    # Display content based on clicked button
    if raw_data_button:
        st.subheader("Raw Dataset")
        st.write(df)

    if summary_stats_button:
        st.subheader("Summary Statistics")
        st.write(df.describe())

    if class_distribution_button:
        st.subheader("Class Distribution")
        class_counts = df["class"].value_counts()
        st.bar_chart(class_counts)

if __name__ == "__main__":
    main()
