import numpy as np

"""
Adjacency matrix:
1.) VxV dimensions, where V is the number of vertices in a graph
2.) A 1 indicates that there is an edge between the indices represented by the dimensions
"""

adj_matrix = np.array([
    [0, 1, 1, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 0],
    [0, 0, 0, 0]
])

print(adj_matrix)