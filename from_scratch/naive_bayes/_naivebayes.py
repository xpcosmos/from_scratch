import numpy as np

class CategoricalNB:
    
    def __init__(self):
        pass
    
    def fit(self, X, y):
        
        y_key, count = np.unique(ytrain, return_counts=True) 
        percent = count / numpy_df.shape[0]
        np.asarray((y_key, percent))[1]


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
        
        prob_4_array = []
        temp_list = {}

        for option in options.keys():
            for array in numpy_df[:5]:
                temp_array = np.array([1])
                for value, prob in zip(array, range(0, len(probs))):
                    index = np.where(options[option][prob][0] == value)
                    percent = options[option][prob][1, index]
                    if percent.size == 0:
                        percent = 0
                    temp_array = np.vstack([temp_array, percent])
                prob_4_array.append(temp_array[1:])
            temp_list[option] = prob_4_array
            
        temp_list
            
        return self
    
    
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