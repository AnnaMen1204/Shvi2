import pickle
import sklearn
from sklearn.linear_model import LinearRegression

def get_message(param):
    model = pickle.load('lr_modelshvi.pkl')
    y_pred = model.predict(param)
    return f"Depth {y_pred [0][0]}"
    return f"Width  {y_pred [0][0]}"
