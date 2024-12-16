import pandas as pd

from .dataloading import Data

obj = Data()
df = obj.dataload('artifacts\breast cancer.csv')

class Cleaner:
     def __init__(self):
      pass


def clean(data = df):

    df = df.drop_duplicates()
    df = df.dropna()
    df.drop('Unnamed: 32', axis = 1, inplace = True)
    return df