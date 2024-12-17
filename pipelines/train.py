import pickle

from model import Model

from src.datasplit import Split

split = Split()
models = Model()

x_train, x_test, y_train, y_test = split.splitter()
grid = models.model()
grid.fit(x_train, y_train)
