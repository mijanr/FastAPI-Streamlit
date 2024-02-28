"""
Train an ML model on Iris dataset
"""
import joblib
from sklearn.linear_model import LogisticRegression
import optuna
import json
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np
import git

base_path = git.Repo('.', search_parent_directories=True).working_tree_dir
params_path = base_path + "/best_params/" + "best_hyper_params" + ".json"
model_path = base_path + "/saved_model/" + "saved_model.joblib"



class IrisModel:
    """
    Train a Logistic Regression model on the Iris dataset
    """
    def __init__(self):
        self.model = None

    def hyperparameter_tuning(self, X, y):
        def objective(trial):
            # hyperparameters to tune for Logistic Regression
            params = {
                'C': trial.suggest_loguniform('C', 0.01, 10),
                'penalty': trial.suggest_categorical('penalty', ['l1', 'l2']),
                'solver': trial.suggest_categorical('solver', ['liblinear', 'saga'])
            }
            model = LogisticRegression(**params)
            model.fit(X, y)
            return model.score(X, y)

        study = optuna.create_study(direction='maximize')
        study.optimize(objective, n_trials=100)
        # export best params as json
        self.hypar_params = params_path
        with open(self.hypar_params, 'w') as f:
            json.dump(study.best_params, f)
        self.best_params = study.best_params
    

    def train(self, X: np.ndarray, y: np.ndarray) -> None:
        """
        Trains the logistic regression model.

        Parameters:
        -----------
        X : array-like of shape (n_samples, n_features)
            The input data.
        y : array-like of shape (n_samples,)
            The target values.

        Returns:
        --------
        None
        """
        # check if best params are available in self.hyparam_params path
        self.hypar_params = params_path
        try:
            with open(self.hypar_params, 'r') as f:
                self.best_params = json.load(f)
            print("Best params loaded")
        except:
            print("Best params not found. Hyperparameter tuning...")
            self.hyperparameter_tuning(X, y)
        self.model = LogisticRegression(**self.best_params)
        self.model.fit(X, y)
        print("Model trained")

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predicts the target values for the input data.

        Parameters:
        -----------
        X : array-like of shape (n_samples, n_features)
            The input data.

        Returns:
        --------
        y : array-like of shape (n_samples,)
            The predicted target values.
        """
        return self.model.predict(X)

    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        """
        Predicts the target probabilities for the input data.

        Parameters:
        -----------
        X : array-like of shape (n_samples, n_features)
            The input data.

        Returns:
        --------
        y : array-like of shape (n_samples, n_classes)
        """
        return self.model.predict_proba(X)

    def save(self):
        """
        Saves the model to disk.
        """
        path = model_path
        joblib.dump(self.model, path)

    def load(self):
        """
        Loads the model from disk.
        """
        self.model = joblib.load(model_path)


if __name__ == "__main__":
    # load data
    iris = load_iris()
    X = iris.data
    y = iris.target

    # split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # train model
    model = IrisModel()
    model.train(X_train, y_train)

    # evaluate model
    print("Test score:", model.model.score(X_test, y_test))

    #save model
    model.save()


