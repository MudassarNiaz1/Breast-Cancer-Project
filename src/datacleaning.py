import pandas as pd

from .dataloading import Data

obj = Data()
df = obj.loader(r'artifacts\breast cancer.csv')

class Cleaner:
    def __init__(self):
      pass


    def clean(self, df = df):
        print(df.shape)
        df = df.drop('Unnamed: 32', axis = 1)

        df = df.drop_duplicates()
        df = df.dropna()
        print(df.shape)
        df.to_csv('./artifacts/data.csv')      # create the file
        return df
    
c = Cleaner()
c.clean()