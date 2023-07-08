import numpy as np

class KNeighborsClassifier:
    def __init__(self, K, normalize = False, encoding = None):
        self.K = K
        self.normalize = normalize # MinMaxScaler, StandardScaler
        self.encoding = encoding  # OneHotEncoder, OrdinalEncoder
    
    