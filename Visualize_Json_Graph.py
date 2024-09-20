import json
import networkx as nx
import matplotlib.pyplot as plt

def visualize_saved_graph(file_name):
    """
    Visualizes the saved graph from the JSON file.

    Args:
    - file_name: The name of the JSON file containing the graph data.
    """
    # Load graph data from JSON file
    with open(file_name, 'r') as json_file:
        graph_data = json.load(json_file)
    
    # Create a directed graph
    G = nx.Graph()

    # Add nodes to the graph
    for node in graph_data['nodes']:
        G.add_node(node['id'], highlighted=node['highlighted'])

    # Add edges to the graph
    for edge in graph_data['edges']:
        G.add_edge(edge['source'], edge['target'], highlighted=edge['highlighted'])
    
    # Set positions based on node positions
    pos = {node['id']: node['position'][::-1] for node in graph_data['nodes']}  # reverse coordinates for visualization

    # Draw the nodes
    highlighted_nodes = [node for node in G.nodes if G.nodes[node]['highlighted']]
    normal_nodes = [node for node in G.nodes if not G.nodes[node]['highlighted']]

    nx.draw_networkx_nodes(G, pos, nodelist=highlighted_nodes, node_color='r', label="Highlighted Nodes")
    nx.draw_networkx_nodes(G, pos, nodelist=normal_nodes, node_color='b', label="Normal Nodes")
    
    # Draw the edges
    highlighted_edges = [(u, v) for u, v in G.edges if G[u][v]['highlighted']]
    normal_edges = [(u, v) for u, v in G.edges if not G[u][v]['highlighted']]

    nx.draw_networkx_edges(G, pos, edgelist=highlighted_edges, edge_color='r', label="Highlighted Edges")
    nx.draw_networkx_edges(G, pos, edgelist=normal_edges, edge_color='b', label="Normal Edges")

    # Draw labels
    nx.draw_networkx_labels(G, pos)

    title = file_name.split('/')[-1].split('.')[0]

    # Display the plot with legend
    plt.legend()
    plt.title(f'{title}')
    plt.axis('off')
    plt.show()
