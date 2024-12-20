import joblib as j

from pipelines.model import Model
from src.datasplit import Split

split = Split()
models = Model()

x_train, x_test, y_train, y_test = split.splitter()
grid = models.model()

print('Starting Training')

grid.fit(x_train, y_train)

print('Model Train')

model = grid.best_estimator_

j.dump(model, 'models/model.pkl')

print('Model Save')
