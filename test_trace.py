#!/usr/bin/env python3
"""Test simple execution trace generation"""

from Parser import parse_graph

def fw_silent(matrix):
    M = [row[:] for row in matrix]
    T = [[0 for _ in range(len(M))] for _ in range(len(M))]
    
    for i in range(len(M)):
        for j in range(len(M)):
            if M[i][j] != float('inf'):
                T[i][j] = i
            else:
                T[i][j] = None
    
    for k in range(len(M)):
        for i in range(len(M)):
            for j in range(len(M)):
                if M[i][j] > M[i][k] + M[k][j]:
                    M[i][j] = M[i][k] + M[k][j]
                    T[i][j] = T[k][j]
    
    for i in range(len(M)):
        if M[i][i] < 0:
            raise ValueError("Negative cycle detected")
    
    return M, T

g = parse_graph('Graphes/1.txt')
L, P = fw_silent(g.matrix)

out = []
out.append("=" * 70)
out.append(f"EXECUTION TRACE - GRAPH 1")
out.append("=" * 70)
out.append(f"\nGraph: {g.n} vertices")
out.append(f"\nFinal Distance Matrix L:")
for row in L:
    out.append(str(row))
out.append(f"\nExecution successful!")

with open('ExecutionTraces/graph_1_trace.txt', 'w') as f:
    f.write('\n'.join(out))

print("✅ Test trace created!")
