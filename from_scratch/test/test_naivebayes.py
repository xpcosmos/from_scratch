#!/usr/bin/env python3
import sys
sys.path.append(r'.')

import numpy as np
from from_scratch.naive_bayes import CategoricalNB
from from_scratch.datasets import adults_dataset


X_train, X_test, y_train, y_test = adults_dataset.load()


model = CategoricalNB()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(model.score(y_test, y_pred))