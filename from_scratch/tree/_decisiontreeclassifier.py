import numpy as np

class DecisionTreeClassifier:
    
    #   Construção de uma árvore de decisão
    #   *   Escolher atributo
    #   *   Estender árvore adicionando ramos de acordo com a partição
    #   *   Passar exemplos para nós
    #   *   Avaliar critério de parada
    
    #   Critério de utilidade de atributo para classificação, ou seja, os atributos devem ser capazes de discriminar as classes
    #   *   Uma divisão que mantêm proporções de classes em todas as partições é inútil 
    #   *   Uma divisão onde cada partição todos os exemplos são da mesma classe tem utilidade máxima.
    
    #   Medida de partição utiliza o método de ganho de informação e índice GINI.
    #   A entropia é a medida de aleatoriedade (grau de pureza de uma variável). O ganho de informação mede a redução
    # da entropia causada pela partição dos exemplos de acordo com os valores do atributo. A entropia de uma variável qualitativa X, com instâncias
    # pertencentes à classe i, com probabilidade pi, é dada por:  
    #                                                            Entropia(X) =  Somatório (pi log2 pi)
     def __init__(self):
          pass