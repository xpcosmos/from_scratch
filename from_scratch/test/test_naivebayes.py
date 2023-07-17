#!/usr/bin/env python3
import sys
sys.path.append(r'.')

import numpy as np
from from_scratch.naive_bayes import CategoricalNB
from from_scratch.datasets import adults_dataset


X_train = adults_dataset.X_train()
X_test = adults_dataset.X_test()
y_train = adults_dataset.y_train()
y_test = adults_dataset.y_test()


model = CategoricalNB()
model.fit(X_train, y_train)
print(model.predict(X_test))