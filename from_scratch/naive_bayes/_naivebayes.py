import numpy as np

class CategoricalNB:
    
    def __init__(self):
        pass
    
    def fit(self, X, y):      
        self.y_keys = self._get_percent_unique(y)
        self.__options = {}
        
        for key in self.y_keys[0]:
            self.__options[key] = self._get_probs(X, y, key)
            
        return self
        
    def predict(self, X):
        predictions = dict()
        # Tem como simplificar para caralho
        for key in self.__options.keys():
            predictions[key] = self._predict(key, X, self.__options)
        predictions = self._set_class_predicted(predictions)
        return predictions
    
    def score(self, y_true, y_pred):
        
        y_true = self._to_numpy(y_true)
        y_pred = self._to_numpy(y_pred)
        
        return np.sum(y_true == y_pred) / y_true.size
        
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

    def _predict(self, key, X, array_prob):
        prediction = []
        for array in X:
            predicted = np.array([1])
            
            for value, prob in zip(array, range(0, len(array_prob[key]))):
                index = np.where(array_prob[key][prob][0] == value)
                
                percent = self._is_percent_zero(array_prob[key][prob][1, index])
                predicted = np.vstack([predicted, percent]) 
            predicted = np.prod(predicted) * self.y_keys[1, np.where(self.y_keys[0] == key)]
            prediction.append(predicted)
        return prediction

    def _get_probs(self, X_to_prob, y_prob, _key):
        probs = list()
        array_temp = X_to_prob[np.where(y_prob == _key)[0]]
        for i in range(0, array_temp.shape[1]):
            key_and_probability = self._get_percent_unique(array_temp[:,i])
            probs.append(key_and_probability)
        return probs
    
    def _set_class_predicted(self, predictions):
        keys = list(predictions.keys())
        predictions_classes = np.array([0])
        for item1, item2 in zip(predictions[keys[0]], predictions[keys[1]]):
            if item1 > item2:
                predictions_classes = np.vstack([predictions_classes, keys[0]])
            elif item2 > item1:
                predictions_classes = np.vstack([predictions_classes, keys[1]])
            else:
                predictions_classes = np.vstack([predictions_classes, None])
        return predictions_classes[1:]
    
