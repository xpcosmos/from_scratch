import numpy as np

class CategoricalNB:
    
    def __init__(self):
        pass
    
    def fit(self, X, y):
        
        y_keys = self._get_percent_unique(y)
        self.options = {}
        
        for key in y_keys[0]:
            self.__options[key] = self._get_probs(X, key)
        
        return self
    

    
    def predict(self, X):
        # Tem como simplificar para caralho
        for key in self.__options.keys():
            predictions[key] = self._predict(key, X, self.__options)
        return predictions
    
    
    # Funções auxiliares 
    def _is_percent_zero(percent):
        if percent.size == 0:
            return 0
        else: 
            return percent
        
    def _get_percent_unique(X):
        key, count = np.unique(X, return_counts=True) 
        percent = count / X.shape[0]
        return  np.asarray((key, percent))
    
    def isnumpy(self, obj):
        return isinstance(obj, np.ndarray)
    
    # Extraindo Probabilidades para cada variável do conjunto de dados original
    # Parâmetros: (Chave, Array X, Array com probabilidades únicas
    #             Array com probabilidades)
    def _predict(self, key, X, array_prob):
        prediction = []
        for array in X:
            predicted = np.array([1])
            for value, prob in zip(array, range(0, array_prob[key].size)):
                index = np.where(array_prob[key][prob][0] == value)
                percent = self._is_percent_zero(array_prob[key][prob][1, index])
                predicted = np.vstack([predicted, percent])[1:]
            prediction.append(predicted)
        return prediction

    

    def _get_probs(self, _obj, key):
        probs = list()
        array_temp = _obj[np.where(_obj[:,-1] == key)]
        for i in range(0, array_temp.shape[1]):
            _key, _count = np.unique(array_temp[:,i], return_counts=True) 
            _percent = _count / array_temp.shape[0]
            key_and_probability = np.asarray((_key, _percent))
            probs.append(key_and_probability)

        
        return probs