import numpy as np

class StandardScaler:
    
    def fit_transform(self, X):
        self.x_meanxs = []
        self.x_stdxs =[]
        
        X_to_transform = X.T
        
        for i in range(0, X_to_transform.shape[0]):
        
            for j in X_to_transform[i]:
                row = [self._transform(v, X_to_transform[i]) for v in X_to_transform[i]]
        
            X_to_transform[i] = row
        return X_to_transform.T
                
            
    def _transform(self, x, X_main):
        x_mean = np.mean(X_main)
        x_std = np.std(X_main)
        
        self.x_meanxs.append(x_mean)
        self.x_stdxs.append(x_std)
        
        x = (x - x_mean) / x_std)
        return x
    
    def invert(self, X):
        
        X_to_invert = X.T
        
        for i in range(0, X_to_invert.shape[0]):
            for j in X_to_invert[i]:
                row = [self._transform(v, X_to_invert[i]) for v in X_to_invert[i]]
        
            X_to_invert[i] = row
        return X_to_invert.T
                
    def invert(self, x, X_main):

        self.x_meanxs.append(x_mean)
        self.x_stdxs.append(x_std)
        
       # x = (x - x_mean) / x_std)
        return x