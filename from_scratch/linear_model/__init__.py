# coding=utf-8
import numpy as np

class LinearRegression:
    
    def __init__(self, positive=False):
        self.positive = positive        
    
    def fit(self, X, y):
        
        # Converte matrizes em arrays numpy
        X = np.array(X)
        y = np.array(y)
        
        # Força coeficiente a serem positivos.
        if self.positive:
            X = np.abs(X)
        
        # Adciona coluna de 1 para representar o intercept
        self.X = np.column_stack((np.ones(np.size(X)), X))
        self.y = y
        # QR decomposition
        Q, R = np.linalg.qr(self.X)
        # Solving equation
        beta = np.linalg.solve(R, np.dot(Q.T, self.y))
        
        self.intercept = beta[0]
        self.coef_ = beta[1]
        return self
        
    def predict(self, X):
        return (self.coef_*X) + self.intercept
    
    def score(X, y):
        pass
