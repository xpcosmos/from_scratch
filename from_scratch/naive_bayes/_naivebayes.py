import numpy as np

class CategoricalNB:
    
    def __init__(self):
        pass
    
    def fit(self, X, y):
        
        probs = list()
        options = {}
        for option in y_key:
            array_temp = numpy_df[np.where(numpy_df[:,-1] == y_key[1])]
            for i in range(0, array_temp.shape[1]):
                key, count = np.unique(array_temp[:,i], return_counts=True) 
                percent = count / array_temp.shape[0]
                count = np.asarray((key, percent))
                probs.append(count)
            options[option] = probs
        options
        
        self.__prob = list()
        for i in range(0, X.shape[1]):
            key, count = np.unique(X[:,i], return_counts=True) 
            percent = count / X.shape[0]
            freq = np.asarray((key, percent))
            self.__X_prob.append(freq)
            
        return self
    
    
    def predict(self, X):
        pass
    
    def isnumpy(self, obj):
        return isinstance(obj, np.ndarray)