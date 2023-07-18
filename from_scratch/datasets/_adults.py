import pandas as pd
import numpy as np


class adults_dataset:

    @staticmethod
    def load():
        X_train = pd.read_csv('from_scratch/datasets/data/adults/X_train.csv').to_numpy()
        X_train = np.delete(X_train, 2, 1)
        
        X_test = pd.read_csv('from_scratch/datasets/data/adults/X_test.csv').to_numpy()
        X_test = np.delete(X_test, 2, 1)
        
        y_train = pd.read_csv('from_scratch/datasets/data/adults/y_train.csv').to_numpy() 
        y_test = pd.read_csv('from_scratch/datasets/data/adults/y_test.csv').to_numpy()

        return X_train, X_test, y_train, y_test
    