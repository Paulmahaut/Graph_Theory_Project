def shortest_path(L, P, sv, ev, n, cities=None):
    """Rebuild and display the shortest path from sv to ev
    
    Args:
        L: Cost matrix
        P: Predecessors matrix
        sv: Starting vertex
        ev: Ending vertex
        n: Number of vertices
        cities: Optional dict mapping vertex indices to city names
    """
    
    # Validate inputs
    if sv < 0 or sv >= n or ev < 0 or ev >= n:
        print(f"Error: Vertices must be in [0, {n-1}]")
        return None
    
    # If no path exists
    if L[sv][ev] == float('inf'):
        if cities:
            print(f"No path from {cities.get(sv, sv)} to {cities.get(ev, ev)}")
        else:
            print(f"No path from {sv} to {ev}")
        return None
    
    # Reconstruct the path
    path = []
    current = ev
    while current != sv:
        path.append(current)
        if P[sv][current] is None:
            print(f"Error: Broken path reconstruction from {sv} to {ev}")
            return None
        current = P[sv][current]
    
    path.append(sv)
    path.reverse()
    
    # Format and display
    cost = L[sv][ev]
    
    if cities:
        # Display with city names
        path_str = " → ".join([cities.get(v, str(v)) for v in path])
        sv_name = cities.get(sv, sv)
        ev_name = cities.get(ev, ev)
        print(f"🚂 Path from {sv_name} to {ev_name}: {path_str}")
        print(f"   Total travel time: {cost} hours")
    else:
        # Display with just numbers
        path_str = " → ".join(map(str, path))
        print(f"Shortest path from {sv} to {ev}: {path_str} with cost {cost}")
    
    return path, cost