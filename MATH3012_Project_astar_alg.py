import osmnx as ox
from heapq import heappop, heappush
import matplotlib.pyplot as plt
import random
import time

def a_star(graph, start, goal):
    def heuristic(node1, node2):
        # cartesian dist. heuristic 
        x1, y1 = graph.nodes[node1]['x'], graph.nodes[node1]['y']
        x2, y2 = graph.nodes[node2]['x'], graph.nodes[node2]['y']
        return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

    open_set = [(0, start)]
    came_from = {}
    g_score = {node: float('inf') for node in graph.nodes}
    g_score[start] = 0

    while open_set:
        current_cost, current_node = heappop(open_set)

        if current_node == goal:
            path = [current_node]
            while current_node in came_from:
                current_node = came_from[current_node]
                path.insert(0, current_node)
            return path

        for neighbor in graph.neighbors(current_node):
            tentative_g_score = g_score[current_node] + graph[current_node][neighbor][0]['length']
            if tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                heappush(open_set, (tentative_g_score + heuristic(neighbor, goal), neighbor))
                came_from[neighbor] = current_node

    return None  # No path found

def plot_graph(graph, path=None):
    fig, ax = ox.plot_graph(graph, node_size=0, show=False, close=False)
    if path:
        path_edges = list(zip(path, path[1:]))
        path_nodes = set(path)
        
        path_edge_colors = ['r' if edge in path_edges else 'w' for edge in graph.edges]
        path_node_colors = ['r' if node in path_nodes else 'w' for node in graph.nodes]
        path_node_size = [15 if node in path_nodes else 5 for node in graph.nodes]
        ox.plot_graph(graph, node_size=path_node_size, show=False, close=False, edge_linewidth=0.01, edge_color=path_edge_colors, node_color=path_node_colors, ax=ax)

    plt.show()

if __name__ == "__main__":
    place_name = "Georgia Institute of Technology, Atlanta, Georgia, USA"

    graph = ox.graph_from_place(place_name, network_type='walk')

    start_node = list(graph.nodes)[0]
    goal_node = random.choice(list(graph.nodes)[1:])
    for _ in range(50):
        # print(graph)
        t0 = time.time()
        path = a_star(graph, start_node, goal_node)
        t = time.time()
        print(t-t0)
    # if path:
        #     print("Optimal Path:", path)

        #     plot_graph(graph, path)
    # else:
    #     print("No path found.")
    #     pass
