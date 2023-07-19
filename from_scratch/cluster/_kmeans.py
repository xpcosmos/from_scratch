import numpy as np

class KMeans:
    def __init__(self, k=3, max_iters = 100, random_state=None, plot_steps=False):
      self.k = k
      self._random_state = random_state
      self.plot_steps = plot_steps
      self.max_iters = max_iters
      
      self.clusters = [[] for _ in range(self.k)]
      # Atributos médios dos clusters
      self.centroids = []
      
    @property
    def random_state(self):
        raise AttributeError('Read Only')
      
    @random_state.setter
    def random_state(self, value):
        if value:
            np.random.seed(value)
        else: 
            value = np.random.randint(0, 100)
            np.random.seed(value)
        self._random_state = value
    
    def predict(self, X):
        self.X = X
        self.num_samples, self.num_features = X.shape
        # inicialização de centroides é baseada em samples aleatórios de X
        random_centroids_idxs = np.random.choice(self.num_samples, self.k, replace=False)
        self.centroids = [self.X[idx] for idx in random_centroids_idxs]
        # Optimização de centroids
        for _ in range(self.max_iters):
            #   Armazenar antigo centroid
            
            #   Extrair centroids
            self.clusters = self._create_clusters(self.centroids)
            old_centroid = self.centroids
            self.centroids = self._get_centroid(self.clusters)
                
            # Checar se centroid convergem
            if self._is_converged(self.centroids, old_centroid):
                break
            
        return self._get_custer_labels
    
    @staticmethod
    def _euclidian_distance(x1, x2):
        try:
            return np.sqrt((x1 - x2) ** 2)
        except(TypeError):
            return 0
    
    # Função que irá atribuir centroid mais próximo a amostra. Utiliza enumarte em X
    def _create_clusters(self, centroid):
        print(self.X)
        clusters = [[] for _ in range(self.k)]
        for idx, sample in enumerate(self.X):
            centroid_idx = self._closest_centroid(sample, centroid)
            clusters[centroid_idx].append(idx)
            
        return clusters
        
    
    # Função que calcula o centroid mais próximo do dado e retorna o índice com np.argmin
    def _closest_centroid(self, sample, centroid):
        
        for s in sample:
            distance = [self._euclidian_distance(s, point) for point in centroid]
        closest_idx = np.argmin(distance)
        return closest_idx
    
    # Inicializa centroid com np_zero, de tamnho k e n_features
    #   Para cada cluster, armazena valor médio de X de cluster
    #   Amazena em lista criada e retorna a lista.
    def _get_centroid(self, clusters):
        
        centroids = np.zeros((self.k, self.num_features))
        for id, cluster in enumerate(clusters):
            cluster_mean = np.mean(self.X[cluster], axis=0)
            centroids[id] = cluster_mean
        return centroids
    
    # Checa de lista criada em _get_centroid convergiu através da distância euclidiana.
    def _is_converged(self, old_centroid, centroid):
        distance = [self._euclidian_distance(old_centroid[i], centroid[i]) for i in range(self.k)]
        return sum(distance) == 0
    
    # Cria array vazio de tamanho n_samples e itera enumarate de clusters e coloca em uma lista
    #   o índice do cluster.
    def _get_custer_labels(self, clusters):
        labels = np.empty(self.num_samples)
        for id, cluster in enumerate(clusters):
            for sample_id in cluster:
                labels[sample_id] = id
        return labels