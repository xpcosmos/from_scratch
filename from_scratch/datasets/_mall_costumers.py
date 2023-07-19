import pandas as pd
import numpy as np 

class mall_costumers:
    
    def load():
        df = pd.read_csv('from_scratch/datasets/data/mall_costumers/Mall_Customers.csv', index_col=None, sep=';').to_numpy()[:,2:]
        return df