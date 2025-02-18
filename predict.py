import joblib
import pandas as pd

# Scaler Load
sc = joblib.load("models\\scaler.pkl")

# Model load
model = joblib.load("models\\model.pkl")

# user data
df = pd.read_csv("artifacts\\data.csv")
data = df.drop(['diagnosis', 'Unnamed: 0'], axis=1)
data = data.head(1).values


def prediction(data, scaler=sc, model=model):
    data = scaler.transform(data)
    predict = model.predict(data)
    return predict



