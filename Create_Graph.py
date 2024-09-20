def create_state_space():
    maze = [
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0]
    ]

    # Initialize graph variables
    Total_Nodes = 0
    Mappings = {}
    k = 1

    # Update maze with IDs and prepare Mappings
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] != 0:
                maze[i][j] = k
                Mappings[(i, j)] = k
                Total_Nodes += 1
                k += 1
            else:
                maze[i][j] = ' '
                Mappings[(i, j)] = 0

    # Function to get valid neighbours of a node
    def create_neighbours(maze, pos):
        links = []
        directions = {
            "up": (pos[0] - 1, pos[1]),
            "down": (pos[0] + 1, pos[1]),
            "left": (pos[0], pos[1] - 1),
            "right": (pos[0], pos[1] + 1)
        }
        for direction in directions.values():
            x, y = direction
            if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != ' ':
                links.append(str(maze[x][y]))
        return links

    # Build the graph
    graph = {}
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] != ' ':
                graph[str(maze[i][j])] = create_neighbours(maze, (i, j))

    return graph


