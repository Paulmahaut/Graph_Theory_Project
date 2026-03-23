#!/usr/bin/env python3
from Parser import parse_graph

def fw_silent(matrix):
    M = [row[:] for row in matrix]
    T = [[0 for _ in range(len(M))] for _ in range(len(M))]
    for i in range(len(M)):
        for j in range(len(M)):
            T[i][j] = i if M[i][j] != float('inf') else None
    for k in range(len(M)):
        for i in range(len(M)):
            for j in range(len(M)):
                if M[i][j] > M[i][k] + M[k][j]:
                    M[i][j] = M[i][k] + M[k][j]
                    T[i][j] = T[k][j]
    for i in range(len(M)):
        if M[i][i] < 0:
            raise ValueError("Negative cycle")
    return M, T

for graph_num in range(1, 14):
    try:
        g = parse_graph(f'Graphes/{graph_num}.txt')
        L, P = fw_silent(g.matrix)
        
        with open(f'ExecutionTraces/graph_{graph_num}_trace.txt', 'w') as f:
            f.write(f"EXECUTION TRACE - GRAPH {graph_num}\n")
            f.write("=" * 60 + "\n\n")
            f.write(f"Vertices: {g.n}\n")
            f.write(f"Status: [OK] Successfully executed\n\n")
            f.write("Final Distance Matrix L:\n")
            for row in L:
                f.write(str(row) + "\n")
            f.write("\nFinal Predecessor Matrix P:\n")
            for row in P:
                f.write(str(row) + "\n")
        
        print(f"[OK] Graph {graph_num}")
    except Exception as e:
        with open(f'ExecutionTraces/graph_{graph_num}_trace.txt', 'w') as f:
            f.write(f"EXECUTION TRACE - GRAPH {graph_num}\n")
            f.write("=" * 60 + "\n")
            f.write(f"ERROR: {str(e)}\n")
        print(f"[ERROR] Graph {graph_num}: {str(e)}")

print("\nDone!")
