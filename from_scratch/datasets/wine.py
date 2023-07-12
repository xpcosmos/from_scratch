import pandas as pd

class wine_dataset:
    
    @property
    def X(self):
        return pd.read_csv('from_scratch/datasets/data/wine/X.csv')
    
    @property
    def y(self):
        return pd.read_csv('from_scratch/datasets/data/wine/y.csv')