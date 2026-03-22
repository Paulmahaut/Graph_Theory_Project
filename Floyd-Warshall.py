from Parser import parse_graph
from MatrixHandler import draw_graph2matrix, draw_matrix

g = parse_graph('Graphes/1.txt')

def floyd_warshall(g):
    # initialize M and T being the distance and predecessor matrices respectively
    M = g.matrix
    T = [[0 for n in range(len(M))] for n in range(len(M))]

    for i in range(len(M)):
        for j in range(len(M)):
            if M[i][j] != float('inf'):
                T[i][j] = i
            else:
                T[i][j] = None

    #draw_matrix(M)
    #draw_matrix(T)

    # compute the matrices M and T for each k from 0 to n
    for k in range(len(M)):
        for i in range(len(M)):
            for j in range(len(M)):
                if M[i][j] > M[i][k] + M[k][j]:
                    M[i][j] = M[i][k] + M[k][j]
                    T[i][j] = T[k][j]
    
    # FUNCTION FAILED
    for i in range(len(M)):
        if M[i][i] < 0:
            raise ValueError("Negative cycle detected")
        return None,None
    
    return M,T

M,T = floyd_warshall(g)
print(M,T)
draw_matrix(M)
draw_matrix(T)