import numpy as np

# criando arrays
a = np.array([1, 2, 3, 4, 5])
print(a)
print(type(a))   # <class 'numpy.ndarray'>

# operações vetorizadas (rápidas!)
print(a * 2)        # [2 4 6 8 10] — multiplica TODOS de uma vez
print(a + 10)       # [11 12 13 14 15]
print(a.mean())     # média
print(a.std())      # desvio padrão
print(a.sum())      # soma

# arrays multidimensionais (matrizes)
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matriz)
print(matriz.shape)   # (3, 3) — 3 linhas, 3 colunas

# array de números aleatórios
aleatorios = np.random.rand(5)
print(aleatorios)
