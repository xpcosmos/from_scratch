import pandas as pd
import numpy as np


class adults_dataset:
    
    
    def X_train():
        df = pd.read_csv('from_scratch/datasets/data/adults/X_train.csv').to_numpy()
        df = np.delete(df, 2, 1)
        return df
    
    
    def y_train():
        df = pd.read_csv('from_scratch/datasets/data/adults/y_train.csv').to_numpy()
        return df
    
    def X_test():
        df = pd.read_csv('from_scratch/datasets/data/adults/X_test.csv').to_numpy()
        df = np.delete(df, 2, 1)
        return df
   
    def y_test():
        df = pd.read_csv('from_scratch/datasets/data/adults/y_test.csv').to_numpy()
        return df
    