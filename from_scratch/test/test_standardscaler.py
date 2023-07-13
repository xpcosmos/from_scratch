#!/usr/bin/env python3
import sys
sys.path.append(r'.')

import numpy as np
from from_scratch.preprocessing import StandardScaler


scaler = StandardScaler()

X_train = np.ones((10, 5)) * np.random.randint(0, 1_000, size = (10,5))
X_transformed = scaler.fit_transform(X_train)
X_inverse = scaler.invert(X_transformed)

print('===================================')
print('---------------- X ----------------\n')
print(X_train)
print('===================================')
print('--------- X-Transformed -----------\n')
print(X_transformed)
print('===================================')
print('----------- X-inverse -------------\n')
print(X_inverse)
print('===================================')