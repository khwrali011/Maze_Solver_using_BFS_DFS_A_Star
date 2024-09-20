import json

def save_graph_to_json(path, file_name='highlighted_graph.json'):
    """
    Saves the resulting graph with path highlighted to a JSON file.

    Args:
    - maze: A 2D list representing the maze structure.
    - path: A list of nodes (as integers) representing the highlighted path.
    - file_name: The name of the output JSON file.
    """

    maze = [
        [1, 2, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 3, ' ', ' ', ' ', 4],
        [' ', 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, ' ', ' ', ' ', ' ', 15, ' ', ' ', ' ', 16],
        [' ', ' ', ' ', ' ', ' ', 17, ' ', ' ', ' ', ' ', 18, 19, 20, 21, 22, 23, ' ', ' ', ' ', 24],
        [' ', ' ', ' ', ' ', ' ', 25, ' ', ' ', ' ', ' ', ' ', ' ', 26, ' ', 27, 28, 29, 30, 31, 32],
        [' ', 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, ' ', ' ', ' ', ' ', ' ', 45, ' '],
        [' ', 46, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 47, ' ', ' ', ' ', ' ', ' ', 48, ' '],
        [' ', 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, ' ', ' ', 64, ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 65, ' ', ' ', 66, 67, 68, ' ', 69, ' '],
        [' ', 70, 71, 72, 73, 74, 75, ' ', 76, 77, 78, 79, 80, ' ', ' ', ' ', 81, 82, 83, ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 84, 85, 86, ' ']
    ]
    
    graph = {
        "nodes": [],
        "edges": [],
        "highlighted_path": []
    }
    
    # Convert the path into a set for quick lookup
    path_set = set(map(int, path))
    
    # Construct nodes
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] != ' ':
                node_id = int(maze[i][j])
                graph["nodes"].append({
                    "id": node_id,
                    "position": (i, j),
                    "highlighted": node_id in path_set
                })
    
    # Example edges: Add your actual edge representation logic here
    # Assuming the graph is fully connected for adjacent cells, add edges.
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] != ' ':
                node_id = int(maze[i][j])
                
                # Check for right neighbor
                if j + 1 < len(maze[0]) and maze[i][j + 1] != ' ':
                    neighbor_id = int(maze[i][j + 1])
                    graph["edges"].append({
                        "source": node_id,
                        "target": neighbor_id,
                        "highlighted": node_id in path_set and neighbor_id in path_set
                    })
                
                # Check for bottom neighbor
                if i + 1 < len(maze) and maze[i + 1][j] != ' ':
                    neighbor_id = int(maze[i + 1][j])
                    graph["edges"].append({
                        "source": node_id,
                        "target": neighbor_id,
                        "highlighted": node_id in path_set and neighbor_id in path_set
                    })
    
    # Add highlighted path
    graph["highlighted_path"] = list(path_set)

    # Save to JSON file
    with open(file_name, 'w') as json_file:
        json.dump(graph, json_file, indent=4)
