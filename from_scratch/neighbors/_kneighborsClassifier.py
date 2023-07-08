import numpy as np

class KNeighborsClassifier:
    def __init__(self, K=3, normalize = False, encoding = None):
        self.K = K
        self.normalize = normalize # MinMaxScaler, StandardScaler
        self.encoding = encoding  # OneHotEncoder, OrdinalEncoder
    
    def fit(self, X, y):
        pass
    
    def predict(self, X):
        pass