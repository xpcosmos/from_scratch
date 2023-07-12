import numpy as np

class KNeighborsClassifier:
    def __init__(self, K=3, normalize = False, encoding = None):
        self.K = K
        self.normalize = normalize # MinMaxScaler, StandardScaler
        self.encoding = encoding  # OneHotEncoder, OrdinalEncoder
    
    def fit(self, X, y):
        pass
    
    def predict(self, X):
        predicted_label = [self._predict(x) for x in X]
        return np.array(predicted_label)

    def _predict(self, x):
        pass