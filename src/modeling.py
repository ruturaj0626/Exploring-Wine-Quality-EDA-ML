#modeling.py

from sklearn.ensemble import RandomForestRegressor
from hyperparameters import RANDOM_FOREST_PARAMS

def train_model(X, y):
    model = RandomForestRegressor(**RANDOM_FOREST_PARAMS)
    model.fit(X, y)
    return model
