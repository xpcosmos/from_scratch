#!/usr/bin/env python3
import sys
sys.path.append(r'.')

import numpy as np
from from_scratch.preprocessing import StandardScaler



X = np.ones((10, 5)) * np.random.randint(0, 1_000, size = (10,5))
print('------------- X ----------------')
print('X-Médio:\t', np.mean(X))
print('Desvio padrão:\t', np.std(X))
print(X)


scaler = StandardScaler()
X_transformed = scaler.fit_transform(X)

print('------- X-Transformed ----------')
print(X_transformed)

X_inverse = scaler.invert(X)

print('------- X-inverse ----------')
print(X_inverse)