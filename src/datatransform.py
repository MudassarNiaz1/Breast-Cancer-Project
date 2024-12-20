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
        x = sc.fit_transform(x)

        return x, y
