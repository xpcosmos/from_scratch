import numpy as np
from collections import Counter

def _distancia_euclidiana(x1, x2):
        distancia = np.sqrt(np.sum(x1 - x2) ** 2)
        return distancia

class KNeighborsClassifier:
    def __init__(self, K=3, normalize = False, encoding = None):
        self.K = K
        self.normalize = normalize # MinMaxScaler, StandardScaler
        self.encoding = encoding  # OneHotEncoder, OrdinalEncoder
    
    def fit(self, X, y):
        self.X = X
        self.y = y
        pass
    
    def predict(self, X):
        predicted_label = [self._predict(x) for x in X]
        return np.array(predicted_label)

    def _predict(self, x):
        # Calculo de distâncias
        prediction = [_distancia_euclidiana(x, x2) for x2 in self.X]
        # Extrair kn de amostras e labels
        k_id = np.argsort(prediction)[:self.K]
        knn_labels = [self.y[i] for i in k_id]
        # Labels mais comuns
        most_comuns = Counter(knn_labels).most_common(1)
        return most_comuns[0][0]

    