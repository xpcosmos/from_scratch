import numpy as np

class StandardScaler:
    
    def fit_transform(self, X):

        self.x_meanxs = []
        self.x_stdxs =[]
        transformed = np.zeros(shape=X.shape)
        for i in range(0, X.shape[1]):
            row = [self._transform(v, X[:,i]) for v in X[:,i]]
            self.x_meanxs.append(np.mean(X[:,i]))
            self.x_stdxs.append(np.std(X[:,i]))
            
            transformed[:,i] = row 
        return transformed
                
    def invert(self, X):
        inverse = np.zeros(shape=X.shape)
        for i in range(0, X.shape[1]):
            row = [self._invert_x(v, self.x_meanxs[i], self.x_stdxs[i]) for v in X[:,i]]
            inverse[:,i] = row
        return inverse
                
    def _invert_x(self, x, xs_mean, xs_std):
        x_inverso = (x*xs_std) + xs_mean
        return x_inverso
    
    def _transform(self, x, X_main):
        x_mean = np.mean(X_main)
        x_std = np.std(X_main)
        
        x = (x - x_mean) / x_std
        return x
    
    
    
                