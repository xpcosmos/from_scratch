import numpy as np

class LinearRegression:

    def _set_coef(self):
        return ((self.n*sum(self.X*self.y)) - (sum(self.X) * sum(self.y)))/ (self.n*sum(self.X**2) - sum(self.X)**2)
 
    def _set_intercept(self):
        return sum(self.y) - ((self.coef_ * sum(self.X)) / self.n)

    
    def fit(self, X, y):
        self.X = X
        self.y = y
        self.n = self.X.shape[0]
        
        self.coef_ = self._set_coef()
        self.intercept_ = self._set_intercept()

    def predict(self, X):
        return (self.coef_*X) + self.intercept_
    
