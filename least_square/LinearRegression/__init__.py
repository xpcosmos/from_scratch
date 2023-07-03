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
    
lr = LinearRegression()
lr.fit(np.array([2,2,3]), np.array([2,5,6]))
print(lr.predict(np.array([2,5])))

# y = m*x + b
# m = n*sum(xy) -sum(x)*sum(y)/ n*sum(x**2) - sum(x)**2
# b = sum(y) - m*sum(x) / n