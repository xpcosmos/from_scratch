import pandas as pd
import numpy as np 

class mall_costumers:
    
    def load(self):
        df = pd.read_csv('from_scratch/datasets/data/mall_costumers/Mall_Customers.csv')
        return df