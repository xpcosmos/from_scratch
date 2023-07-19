import numpy as np

class KMeans:
    def __init__(self, k=3, max_iters = 100, random_state=None, plot_steps=False):
      self.k = k
      self.random_state = random_state
      self.plot_steps = plot_steps
      
      self.clusters = [[] for _ in range(self.k)]
      # Atributos médios dos clusters
      self.centroids = []
      
    
    def predict(self, X)