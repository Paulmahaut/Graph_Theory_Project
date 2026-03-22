import math
import tabulate
from Parser import parse_graph

g = parse_graph('Graphes/1.txt')

def draw_graph2matrix(g):
    table = [[None]]
    table[0] += [i for i in range(g.n)]
    for i in range(g.n):
        row = [i]
        for j in range(g.n):
            if g.matrix[i][j] == math.inf:
                row.append('∞')
            else:
                row.append(g.matrix[i][j])
        table.append(row)
    print(tabulate.tabulate(table, tablefmt='grid'))

def draw_matrix(m):
    print(tabulate.tabulate(m, tablefmt='grid'))
