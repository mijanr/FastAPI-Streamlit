"""
Iris dataset pair plot
"""
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests
import git

basePath = git.Repo('.', search_parent_directories=True).working_tree_dir
dataPath = basePath + "/data/iris.csv"

# # get the head data from fastapi endpoint /iris
# url = "http://127.0.0.1:8000/iris"
# r = requests.get(url)
# df = pd.DataFrame(r.json())
df = pd.read_csv(dataPath)

# darkgrid
sns.set_style("darkgrid")

# display the pair plot
st.title("Iris dataset pair plot")
fig, ax = plt.subplots()
fig = sns.pairplot(df, hue="species", kind="reg")
st.pyplot(fig)
