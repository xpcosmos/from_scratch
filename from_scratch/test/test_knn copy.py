#!/usr/bin/env python3
import sys
sys.path.append(r'.')

from from_scratch.cluster import KMeans
from from_scratch.datasets._mall_costumers import mall_costumers

X = mall_costumers.load()
print(X)

model = KMeans(k =3, max_iters=100, random_state=123)
model.predict(X)