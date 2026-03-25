import numpy as np
from scipy.sparse.csgraph import dijkstra
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse.csgraph import bellman_ford
from scipy.sparse.csgraph import depth_first_order
from scipy.sparse.csgraph import breadth_first_order
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr = csr_matrix(arr)

print(dijkstra(newarr, return_predecessors=True, indices=0))

print(floyd_warshall(newarr, return_predecessors=True))

print(bellman_ford(newarr, return_predecessors=True, indices=0))

print(depth_first_order(newarr, 1))

print(breadth_first_order(newarr, 1))