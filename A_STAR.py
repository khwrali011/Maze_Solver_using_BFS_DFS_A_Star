import heapq

def a_star_all_paths(graph, start_node, end_node):
    def heuristic(node, goal):
        # Placeholder heuristic; can be adjusted for specific use cases
        return 0
    
    # Priority queue (min-heap) for exploring nodes
    open_set = []
    heapq.heappush(open_set, (0, start_node))  # (priority, node)
    
    # Cost to reach the node
    g_cost = {start_node: 0}
    # Estimated total cost (g + h)
    f_cost = {start_node: heuristic(start_node, end_node)}
    
    # Parent dictionary to reconstruct the path
    parent = {start_node: None}
    # To track all possible paths
    paths = {start_node: [[start_node]]}
    
    while open_set:
        _, current_node = heapq.heappop(open_set)
        
        if current_node == end_node:
            # Collect all paths to end_node
            all_paths = paths.get(end_node, [])
            # print("All Possible Paths to {}:".format(end_node))
            # for path in all_paths:
            #     print(path)
            
            # Find and return the shortest path based on length
            shortest_path = min(all_paths, key=len)
            return shortest_path
        
        # Explore neighbors
        for neighbor in graph.get(current_node, []):
            new_g_cost = g_cost[current_node] + 1  # Assuming uniform edge cost of 1
            if neighbor not in g_cost or new_g_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_g_cost
                f_cost[neighbor] = new_g_cost + heuristic(neighbor, end_node)
                parent[neighbor] = current_node
                
                if neighbor not in paths:
                    paths[neighbor] = []
                
                # Extend the paths
                for path in paths[current_node]:
                    new_path = path + [neighbor]
                    paths[neighbor].append(new_path)
                
                heapq.heappush(open_set, (f_cost[neighbor], neighbor))
    
    # If no path is found
    return []
