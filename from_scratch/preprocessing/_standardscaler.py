import numpy as np

class StandardScaler:
    
    def fit_transform(self, X):
        self.x_meanxs = []
        self.x_stdxs =[]
        
        X_to_transform = X.T
        
        for i in range(0, X_to_transform.shape[0]):
            row = [self._transform(v, X_to_transform[i]) for v in X_to_transform[i]]
            self.x_meanxs.append(np.mean(X_to_transform[i]))
            self.x_stdxs.append(np.std(X_to_transform[i]))
            X_to_transform[i] = row
        return X_to_transform.T
                
            
    def _transform(self, x, X_main):
        x_mean = np.mean(X_main)
        x_std = np.std(X_main)
        
        x = (x - x_mean) / x_std
        return x
    
    def invert(self, X):

        
        X_to_invert = X.T
        
        for i in range(0, X_to_invert.shape[0]):
            row = [self._invert_x(v, self.x_meanxs[i], self.x_stdxs[i]) for v in X_to_invert[i]]
            X_to_invert[i] = row
        return X_to_invert.T
                
                
    def _invert_x(self, x, xs_mean, xs_std):
        x_inverso = (x*xs_std) + xs_mean
        return x_inverso