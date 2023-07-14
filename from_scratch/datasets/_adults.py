import pandas as pd

class adults_dataset:
    
    @property
    def X_train(self):
        return pd.read_csv('from_scratch/datasets/data/adults/X_train.csv')
    
    @property
    def y_train(self):
        return pd.read_csv('from_scratch/datasets/data/adults/y_train.csv')
    @property
    def X_test(self):
        return pd.read_csv('from_scratch/datasets/data/adults/X_test.csv')
    @property
    def y_test(self):
        return pd.read_csv('from_scratch/datasets/data/adults/y_test.csv')
    