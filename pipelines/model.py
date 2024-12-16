from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

Rf = RandomForestClassifier()

class Model:
    def __init__(self):
        pass
    def model(self):
        params = {
            'n_estimators': [1,10,20,30,40,50],
            'criterion': ['gini', 'entropy','log_loss'],
            'max_depth': [50],
            'min_samples_split' : [2],
            'max_features': ['sqrt','sqrt']
        }

        grid =  GridSearchCV(estimator=Rf, cv=5, scoring='accuracy', param_grid=params)

        return grid