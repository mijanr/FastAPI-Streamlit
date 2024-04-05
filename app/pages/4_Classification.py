"""
Create a Streamlit app that takes in features about the iris flower and returns the species of the flower.
"""
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
import requests
import joblib
import git

basePath = git.Repo('.', search_parent_directories=True).working_tree_dir
modelPath = basePath + "/saved_model/saved_model.joblib"

def load_data():
    iris = load_iris()
    X = iris.data
    y = iris.target
    return X, y


def app():
    
    # Add title and description
    st.title("Predicting Iris Flower Species")

    # Sidebar with input fields
    sepal_length = st.slider("Sepal Length", 0.0, 10.0, 5.0)
    sepal_width = st.slider("Sepal Width", 0.0, 10.0, 5.0)
    petal_length = st.slider("Petal Length", 0.0, 10.0, 5.0)
    petal_width = st.slider("Petal Width", 0.0, 10.0, 5.0)

    # Create input data (dictionary)
    input_data = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }

    # # interact with FastAPI endpoint
    # response = requests.post("http://127.0.0.1:8000/predict", json=input_data)
    model = joblib.load(modelPath)


    target_names = ['Setosa', 'Versicolor', 'Virginica']
    if st.button("Predict"):
        # # make a post request to the FastAPI endpoint
        # prediction = int(response.json()[0])
        # pred_prob = response.json()[1]

        # # print results
        # st.write(f"Species predicted: {target_names[prediction]} with {pred_prob:.2f}% confidence")
        prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])[0]
        pred_prob = model.predict_proba([[sepal_length, sepal_width, petal_length, petal_width]]).max()*100
        st.write(f"Species predicted: {target_names[prediction]} with {pred_prob:.2f}% confidence")
    # We will plot how the train data clusters in 2D space and then see how the test data fits in it.
    # First apply PCA to reduce the dimensionality of the data to 2D
    X, y = load_data()
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)

    data_test = [[sepal_length, sepal_width, petal_length, petal_width]]
    data_test = pca.transform(data_test)

    # add class labels as legend
    fig, ax = plt.subplots()
    for i in range(3):
        ax.scatter(X_pca[y==i, 0], X_pca[y==i, 1], label=target_names[i])
        
    # Use "test_data" as label for the test data
    ax.scatter(data_test[:, 0], data_test[:, 1], c='red', marker='x', s=100, label='test_data')
    ax.set_xlabel('First Principal Component')
    ax.set_ylabel('Second Principal Component')
    ax.set_title('Train data')
    ax.legend()
    st.pyplot(fig)

if __name__ == "__main__":
    app()