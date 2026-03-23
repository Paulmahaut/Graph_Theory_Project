#!/usr/bin/env python3
"""Generate execution traces for graphs 1-13"""

from Parser import parse_graph
import math

def floyd_warshall_silent(g):
    """Floyd-Warshall without intermediate prints"""
    M = [row[:] for row in g.matrix]
    T = [[0 for n in range(len(M))] for n in range(len(M))]
    
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

def generate_trace(graph_num):
    """Generate execution trace for a single graph"""
    
    filename = f'Graphes/{graph_num}.txt'
    
    try:
        g = parse_graph(filename)
    except FileNotFoundError:
        return None
    
    trace = []
    trace.append("=" * 70)
    trace.append(f"EXECUTION TRACE - GRAPH #{graph_num}")
    trace.append("=" * 70)
    trace.append(f"\n📊 Graph Information:")
    trace.append(f"   Number of vertices: {g.n}")
    trace.append(f"   Graph file: {filename}")
    
    # Count edges
    edge_count = 0
    for i in range(g.n):
        for j in range(g.n):
            if g.matrix[i][j] != float('inf'):
                edge_count += 1
    trace.append(f"   Number of edges: {edge_count}")
    
    trace.append(f"\n📈 Initial Adjacency Matrix (Input A[0]):")
    trace.append(format_matrix(g.matrix))
    
    try:
        L, P = floyd_warshall_silent(g)
        
        trace.append(f"\n✅ Floyd-Warshall Algorithm Completed Successfully!")
        trace.append(f"\n🎯 Final Results:")
        trace.append(f"\nFinal Distance Matrix L (Lk where k={g.n-1}):")
        trace.append(format_matrix(L))
        
        trace.append(f"\nFinal Predecessor Matrix P (Pk where k={g.n-1}):")
        trace.append(format_predecessor_matrix(P))
        
        trace.append(f"\n📊 Analysis:")
        trace.append(f"   ✓ Algorithm converged")
        trace.append(f"   ✓ No absorbing circuits detected")
        trace.append(f"   ✓ All shortest paths computed")
        
    except ValueError as e:
        trace.append(f"\n❌ Algorithm Error:")
        trace.append(f"   ⚠️ {str(e)}")
    
    trace.append("\n" + "=" * 70 + "\n")
    
    return "\n".join(trace)

def format_matrix(matrix):
    """Format a matrix nicely"""
    n = len(matrix)
    lines = []
    
    # Header
    header = "     "
    for j in range(n):
        header += f"{j:8d} "
    lines.append(header)
    lines.append("   " + "─" * (9 * n + 1))
    
    # Rows
    for i in range(n):
        row = f" {i:2d} │ "
        for j in range(n):
            val = matrix[i][j]
            if val == float('inf'):
                row += "    ∞   "
            else:
                row += f"{val:7.1f} "
        lines.append(row)
    
    return "\n".join(lines)

def format_predecessor_matrix(matrix):
    """Format predecessor matrix nicely"""
    n = len(matrix)
    lines = []
    
    # Header
    header = "     "
    for j in range(n):
        header += f"{j:6d} "
    lines.append(header)
    lines.append("   " + "─" * (7 * n + 1))
    
    # Rows
    for i in range(n):
        row = f" {i:2d} │ "
        for j in range(n):
            val = matrix[i][j]
            if val is None:
                row += " None "
            else:
                row += f" {val:4d} "
        lines.append(row)
    
    return "\n".join(lines)

# Generate traces for all graphs 1-13
print("Generating execution traces for graphs 1-13...\n")
for i in range(1, 14):
    trace = generate_trace(i)
    if trace:
        # Save to file
        output_file = f'ExecutionTraces/graph_{i}_trace.txt'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(trace)
        print(f"✅ Graph {i:2d}: Trace saved to ExecutionTraces/graph_{i}_trace.txt")
    else:
        print(f"❌ Graph {i:2d}: File not found")

print("\n🎉 All traces generated successfully!")
