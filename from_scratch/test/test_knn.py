#!/usr/bin/env python3
import sys
sys.path.append(r'.')

from from_scratch.neighbors import KNeighborsClassifier
from from_scratch.datasets.wine import wine_dataset

df = wine_dataset()
print(df)
KNeighborsClassifier()