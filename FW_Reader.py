def shortest_path(L, P, sv, ev, n):
    """Rebuild and display the shortest path from ev to sv"""
    
    # Correct inputs
    if sv < 0 or sv >= n or ev < 0 or ev >= n:
        print(f"Error: Vertices must be in [0, {n-1}]")
        return None
    
    # If no path
    if L[sv][ev] == float('inf'):
        print(f"No path from {sv} to {ev}")
        return None
    
    # Rebuild of the path
    path = []
    current = ev
    while current != sv:
        path.append(current)
        if P[sv][current] is None:
            print(f"Error: No path from {sv} to {ev}")
            return None
        current = P[sv][current]
    
    path.append(sv)
    path.reverse()
    
    # Display and return
    path_str = " -> ".join(map(str, path))
    cost = L[sv][ev]
    print(f"Shortest path from {sv} to {ev}: {path_str} with cost {cost}")
    return path, cost