from Graph import Graph

def parse_graph(filename):
# Parses a graph from a file. The file format is as follows:
    with open(filename, 'r') as f:
        n = int(f.readline())
        m = int(f.readline())
        g = Graph(n)
        for _ in range(m):
            u, v, w = map(int, f.readline().split())
            g.add_arc(u, v, w)
    return g