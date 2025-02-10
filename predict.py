import joblib
import pandas as pd

# Scaler Load
sc = joblib.load("models\\scaler.pkl")

# Model load
model = joblib.load("models\\model.pkl")

# test data
df = pd.read_csv("artifacts\\data.csv")
data = df.drop(['diagnosis', 'id'], axis=1)
data = data.head(1).values


def prediction(data=data, scaler=sc, model=model):
    # data = sc.tranform(data)
    predict = model.predict(data)
    return predict

print(prediction())