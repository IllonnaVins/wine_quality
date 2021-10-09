import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def fit_model(X, y, model, random_seed=42, test_size=0.2, show_results=False, X_test=None, y_test=None, prin=True):
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=test_size, random_state=random_seed)

    model.fit(X_train, y_train)

    if show_results:
        pred_values_test = model.predict(X_test)

        print('TEST SET')
        print('Error RMSE: {}'.format(mean_squared_error(y_test, pred_values_test) ** 0.5))
        print('Score: {}'.format(model.score(X_test, y_test)))

    else:
        pred_values_train = model.predict(X_train)
        pred_values_val = model.predict(X_val)

        if prin:
            print('TRAIN SET')
            print('Error RMSE: {}'.format(mean_squared_error(y_train, pred_values_train) ** 0.5))
            print('Score: {}'.format(model.score(X_train, y_train)))
            print()
            print('VALIDATION SET')
            print('Error RMSE: {}'.format(mean_squared_error(y_val, pred_values_val) ** 0.5))
            print('Score: {}'.format(model.score(X_val, y_val)))
        else:
            return mean_squared_error(y_val, pred_values_val) ** 0.5
