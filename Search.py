import cv2 # type: ignore
from Create_Graph import create_state_space
from BFS import bfs_all_paths
from DFS import dfs_all_paths
from A_STAR import a_star_all_paths
from Visaulize_Path import visualize_path, path_mapping
from Json_Graph import save_graph_to_json
from Visualize_Json_Graph import visualize_saved_graph

state_space = create_state_space()

start_state = "2"
goal_state = "86"

print("\n\nPress 'q' to close windows...")

# BFS Path Visualization
bfs_shortest_path = bfs_all_paths(state_space, start_state, goal_state)
save_graph_to_json(bfs_shortest_path, file_name='./Json_Graphs/BFS.json')
visualize_saved_graph(file_name='./Json_Graphs/BFS.json')
bfs_shortest_node_path = path_mapping(bfs_shortest_path)
print()
print("Shortest Path using BFS: \n{}".format(bfs_shortest_node_path))
print()
visualize_path(bfs_shortest_path, "BFS", "./results_images/bfs_path.png")

# DFS Path Visualization
dfs_shortest_path = dfs_all_paths(state_space, start_state, goal_state)
save_graph_to_json(dfs_shortest_path, file_name='./Json_Graphs/DFS.json')
visualize_saved_graph(file_name='./Json_Graphs/DFS.json')
dfs_shortest_node_path = path_mapping(dfs_shortest_path)
print()
print("Shortest Path using DFS: \n{}".format(dfs_shortest_node_path))
print()
visualize_path(dfs_shortest_path, "DFS", "./results_images/dfs_path.png")

# A* Path Visualization
a_star_shortest_path = a_star_all_paths(state_space, start_state, goal_state)
save_graph_to_json(a_star_shortest_path, file_name='./Json_Graphs/A_STAR.json')
visualize_saved_graph(file_name='./Json_Graphs/A_STAR.json')
a_star_shortest_node_path = path_mapping(a_star_shortest_path)
print()
print("Shortest Path using A*: \n{}".format(a_star_shortest_node_path))
print()
visualize_path(a_star_shortest_path, "A*", "./results_images/a_star_path.png")

# Wait for user to press 'q' to close all windows
while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()  # Close all open windows
        break
