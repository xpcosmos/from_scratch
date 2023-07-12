#!/usr/bin/env python3
import sys
sys.path.append(r'.')

from from_scratch.neighbors import KNeighborsClassifier
from from_scratch.datasets.wine import wine_dataset

X = wine_dataset().X
y = wine_dataset().y


model = KNeighborsClassifier(K=3)