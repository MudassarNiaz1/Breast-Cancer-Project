import joblib
from sklearn.preprocessing import LabelEncoder, StandardScaler

from .datacleaning import Cleaner

cleaner = Cleaner()
df = cleaner.clean()


class Transform:
    def __init__(self):
        pass

    def transformer(self):

        le = LabelEncoder()
        df['diagnosis'] = le.fit_transform(df['diagnosis'])

        x = df.drop('diagnosis', axis = 1)
        y = df['diagnosis']

        sc = StandardScaler()
        sc.fit(x)
        joblib.dump(sc, "models/scaler.pkl")
        x = sc.transform(x)

        return x, y
