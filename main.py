import numpy as np
from from_scratch.linear_model import LinearRegression

X = [1,2,3,4,5,6,7]
y = [1.5, 3.8, 6.7, 9.0, 11.2, 13.6, 16]

X = np.array(X)

model = LinearRegression()
beta = model.fit(X,y)
print(beta)
print(model.coef_)