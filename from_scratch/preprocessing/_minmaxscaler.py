import numpy as np

class MinMaxScaler:
    
    def fit_transform(self, X):
        X = X.T
        for i in range(0, X.shape[0]):
            for j in X[i]:
                row = [self._transform(v, X[i]) for v in X[i]]
            X[i] = row
        return X.T
                
            
    def _transform(self, x, X_main):
        x = (x - np.min(X_main)) / (np.max(X_main) - np.min(X_main))
        return x