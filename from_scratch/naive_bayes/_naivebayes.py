import numpy as np

class CategoricalNB:
    
    def __init__(self):
        pass
    
    def fit(self, X, y):      
        print(X)
        y_keys = self._get_percent_unique(y)
        self.__options = {}
        
        for key in y_keys[0]:
            self.__options[key] = self._get_probs(X, y, key)
        
        
        return self
    

    
    def predict(self, X):
        predictions = dict()
        # Tem como simplificar para caralho
        for key in self.__options.keys():
            predictions[key] = self._predict(key, X, self.__options)
        return predictions
    
    
    # Funções auxiliares 
    def _is_percent_zero(self,percent):
        if percent.size == 0:
            return 0
        else: 
            return percent
        
    def _get_percent_unique(self, _obj):
        _obj = self._to_numpy(_obj)
        key, count = np.unique(_obj, return_counts=True) 
        percent = count / _obj.shape[0]
        return np.asarray((key, percent))
    
    
    def _to_numpy(self, obj):
        if not isinstance(obj, np.ndarray):
            obj =  np.array(obj)
        return obj
    # Extraindo Probabilidades para cada variável do conjunto de dados original
    # Parâmetros: (Chave, Array X, Array com probabilidades únicas
    #             Array com probabilidades)
    def _predict(self, key, X, array_prob):
        prediction = []
        for array in X:
            predicted = np.array([1])
            
            for value, prob in zip(array, range(0, len(array_prob[key]))):
                index = np.where(array_prob[key][prob][0] == value)
                
                percent = self._is_percent_zero(array_prob[key][prob][1, index])
                predicted = np.vstack([predicted, percent])
            prediction.append(predicted[1:])
        return prediction

    def _get_probs(self, X_to_prob, y_prob, _key):
        probs = list()
        array_temp = X_to_prob[np.where(y_prob == _key)[0]]
        for i in range(0, array_temp.shape[1]):
            key_and_probability = self._get_percent_unique(array_temp[:,i])
            probs.append(key_and_probability)
        return probs