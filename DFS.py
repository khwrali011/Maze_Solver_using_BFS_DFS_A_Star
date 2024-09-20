def dfs_all_paths(graph, start_node, end_node):
    def dfs(node, path):
        # If the current node is the end node, record the path
        if node == end_node:
            all_paths.append(path)
            return
        
        # Explore neighbors
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                dfs(neighbor, path + [neighbor])
                visited.remove(neighbor)  # Backtrack

    all_paths = []
    visited = set()
    visited.add(start_node)
    dfs(start_node, [start_node])
    
    # Print all possible paths to the end_node
    if all_paths:
        # print("All Possible Paths to {}:".format(end_node))
        # for path in all_paths:
        #     print(path)
        
        # Find and return the shortest path based on length
        shortest_path = min(all_paths, key=len)
        return shortest_path
    else:
        return []  # Return an empty list if no path is found



