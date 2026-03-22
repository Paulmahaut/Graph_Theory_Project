import math

class Graph:
    def __init__(self, n):
        self.n = n
        self.matrix = [[math.inf] * n for _ in range(n)]

    def add_arc(self, u, v, w):
        self.matrix[u][v] = w