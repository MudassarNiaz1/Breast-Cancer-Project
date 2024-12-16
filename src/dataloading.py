import pandas as pd


class Data:
    def __init__(self):
       pass

    def dataload(self, path):
       data = pd.read_csv(path)
       return data