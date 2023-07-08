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
    
    def score(self, X, y):
        m_x = np.mean(X)
        m_y = np.mean(y)
        S_xy = 0
        S_xx = 0
        S_yy = 0 
        
        for i in range(0, np.size(X)):
            S_xy = S_xy + (X[i] - m_x) * (y[i] - m_y)
            S_xx = S_xx + (X[i] - m_x) ** 2
            S_yy = S_yy + (y[i] - m_y) ** 2
            
        R2 = (S_xy ** 2)/(S_xx * S_yy)
        return R2
