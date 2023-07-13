import numpy as np

class StandardScaler:
    
    def fit_transform(self, X_to_transform):
        
        X_to_transform = X_to_transform.T
        
        for i in range(0, X_to_transform.shape[0]):
        
            for j in X_to_transform[i]:
                row = [self._transform(v, X_to_transform[i]) for v in X_to_transform[i]]
        
            X_to_transform[i] = row
        return X_to_transform.T
                
            
    def _transform(self, x, X_main):
        x = ((x - np.mean(X_main)) / np.std(X_main))
        return x
    
    def invert(self):
        pass