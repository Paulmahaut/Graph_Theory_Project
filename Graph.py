import math

class Graph:
    # A class representing a directed graph using an adjacency matrix.
    def __init__(self, n):
        self.n = n
        self.matrix = [[math.inf] * n for _ in range(n)]

    def add_arc(self, u, v, w):
        # Adds a directed arc from vertex u to vertex v with weight w.
        self.matrix[u][v] = w