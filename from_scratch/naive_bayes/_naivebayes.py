import numpy as np

class CategoricalNB:
    
    def __init__(self):
        pass
    
    def fit(self, X, y):
        
        y_key = self._get_percent_unique(self, y)


        self.probs = list()
        self.options = {}
        for key in y_key[0]:
            array_temp = X[np.where(X[:,-1] == key)]
            for i in range(0, array_temp.shape[1]):
                X_prob = self._get_percent_unique(X[:,i])
                self.probs.append(X_prob)
            self.options[key] = self.probs
        
        
        prob_4_array = []
        dict_probs = {}

        
        for option in y_key[0]:
            for array in X:
                prob_x_key = self._get_prob_ranks(option, array, self.probs, self.options)
                prob_4_array.append(prob_x_key)
            dict_probs[option] = prob_4_array

        return self
    
    def _get_prob_ranks(self, key, array, array_prob, array_with_options):
        temp_array = np.array([1])
        for value, prob in zip(array, range(0, len(array_prob))):
            index = np.where(array_with_options[key][prob][0] == value)
            percent = self.is_percent_zero(self.options[key][prob][1, index])
        return np.vstack([temp_array, percent])[1:]

    
    def is_percent_zero(percent):
        if percent.size == 0:
            return 0
        else: 
            return percent
        
    def _get_percent_unique(self, X):
        key, count = np.unique(X, return_counts=True) 
        percent = count / X.shape[0]
        return  np.asarray((key, percent))
    
    def _get_probs_X(self, X, y_key):
        self.probs = list()
        self.options = {}
        
        for key in y_key:
            array_temp = X[np.where(X[:,-1] == y_key[1])]
            for i in range(0, array_temp.shape[1]):
                key, count = np.unique(array_temp[:,i], return_counts=True) 
                percent = count / array_temp.shape[0]
                count = np.asarray((key, percent))
                self.probs.append(count)
            self.options[key] = self.probs
        self.options
    
    def predict(self, X):
        # Tem como simplificar para caralho
        prob_4_array = []
        temp_list = {}

        for option in options.keys():
            a = 0
            for array in numpy_df[:14,:-1]:
                a+=1
                temp_array = np.array([1])
                for value, prob in zip(array, range(0, len(probs))):
                    index = np.where(options[option][prob][0] == value)
                    percent = options[option][prob][1, index]
                    if not percent.size != 0:
                        percent = 0
                    temp_array = np.vstack([temp_array, percent])
                    
                prob_4_array.append(temp_array[1:])
            temp_list[option] = prob_4_array

        temp_list
    
    def isnumpy(self, obj):
        return isinstance(obj, np.ndarray)