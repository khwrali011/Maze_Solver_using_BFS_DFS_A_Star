def bfs_all_paths(graph, start_node, end_node):
    # Initialize structures
    frontier = [start_node]
    visited = set()
    paths = {start_node: [[start_node]]}  # Store all possible paths to each node

    while frontier:
        selected_node = frontier.pop(0)
        
        if selected_node in visited:
            continue
        
        # Mark the node as visited
        visited.add(selected_node)
        
        # Explore neighbors
        for neighbor in graph.get(selected_node, []):
            if neighbor not in visited:
                if neighbor not in frontier:
                    frontier.append(neighbor)
                
                # Update paths
                if neighbor not in paths:
                    paths[neighbor] = []
                
                # Extend the paths
                for path in paths[selected_node]:
                    new_path = path + [neighbor]
                    paths[neighbor].append(new_path)

    # Print all possible paths to the end_node
    if end_node in paths:
        all_paths = paths[end_node]
        # print("All Possible Paths to {}:".format(end_node))
        # for path in all_paths:
        #     print(path)
        
        # Find and return the shortest path based on length
        shortest_path = min(all_paths, key=len)
        return shortest_path
    else:
        return []  # Return an empty list if no path is found
