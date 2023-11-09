import networkx as nx
import queue
import time
import random
class Temporal_Spatial_Graph:
    def __init__(self):
        self.graph = nx.Graph()
        self.node_count = 0

    def add_node(self):
        node_name = f"p{self.node_count}"
        self.graph.add_node(node_name, spatial_length=(0, 0))  # Default spatial length is set to (0, 0)
        self.node_count += 1

    def add_edge(self, node1, node2, temporal_length, spatial_length):
        self.graph.add_edge(node1, node2, temporal_length=temporal_length, spatial_length=spatial_length)

    def __str__(self):
        return str(self.graph)


class AStarPathfinding:
    def __init__(self, graph):
        self.graph = graph

    def heuristic(self, node, goal):
        # Physical distance example, not implemented yet
        # x1, y1 = self.graph.graph.nodes[node]['spatial_length']
        # x2, y2 = self.graph.graph.nodes[goal]['spatial_length']
        # spatial_distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        # return spatial_distance
        return 0

    def astar(self, start_node, goal_node):
        start_time = time.time()
        open_set = queue.PriorityQueue()
        open_set.put((0, start_node))
        closed_set = set()
        came_from = {}  # Dictionary to store the previous node in the optimal path
        g_score = {node: float('inf') for node in self.graph.graph.nodes}
        g_score[start_node] = 0
        f_score = {node: float('inf') for node in self.graph.graph.nodes}
        f_score[start_node] = self.heuristic(start_node, goal_node)

        while not open_set.empty():
            _, current_node = open_set.get()

            if current_node == goal_node:
                path = [goal_node]
                while current_node != start_node:
                    current_node = came_from[current_node]
                    path.append(current_node)
                end_time = time.time()
                print(end_time-start_time)
                return path[::-1]

            closed_set.add(current_node)

            for neighbor in self.graph.graph.neighbors(current_node):
                if neighbor in closed_set:
                    continue

                tentative_g_score = g_score[current_node] + self.graph.graph[current_node][neighbor]['spatial_length']

                if tentative_g_score < g_score[neighbor]:
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic(neighbor, goal_node)
                    open_set.put((f_score[neighbor], neighbor))
                    came_from[neighbor] = current_node

        return None
    def extract_edges_from_path(self, path):
        if (len(path) == 1):
            return [2*path[0]]
        edges = []
        for i in range(len(path) - 1):
            edge = path[i] + path[i + 1]
            edges.append(edge)
        return edges
# Example Usage
if __name__ == "__main__":
    my_graph = Temporal_Spatial_Graph()
    pf = AStarPathfinding(my_graph)

    # for i in range(100):
    #     my_graph.add_node()

    # my_graph.add_edge("p0", "p1", temporal_length=10, spatial_length=2.5)
    # my_graph.add_edge("p1", "p2", temporal_length=15, spatial_length=3.0)
    # my_graph.add_edge("p0", "p3", temporal_length=8, spatial_length=1.5)
    # my_graph.add_edge("p3", "p4", temporal_length=12, spatial_length=2.0)
    # my_graph.add_edge("p2", "p5", temporal_length=5, spatial_length=1.0)
    # my_graph.add_edge("p5", "p6", temporal_length=20, spatial_length=4.0)
    # my_graph.add_edge("p4", "p7", temporal_length=18, spatial_length=3.5)
    # my_graph.add_edge("p7", "p8", temporal_length=7, spatial_length=1.2)
    # my_graph.add_edge("p1", "p9", temporal_length=25, spatial_length=5.0)
    # my_graph.add_edge("p6", "p9", temporal_length=22, spatial_length=4.2)
    for i in range(100):
        my_graph.add_node()

    # Connect nodes randomly
    for i in range(100):
        # Choose a random number of connections for each node
        num_connections = random.randint(1, 50)

        # Connect the current node to a random set of other nodes
        for _ in range(num_connections):
            target_node = random.choice(list(my_graph.graph.nodes))
            temporal_length = random.randint(1, 30)  # Adjust the range based on your requirements
            spatial_length = round(random.uniform(1.0, 10.0), 1)  # Adjust the range based on your requirements
            my_graph.add_edge(f"p{i}", target_node, temporal_length=temporal_length, spatial_length=spatial_length)


    start_node = "p0"
    goal_node = "p99"
    path = pf.astar(start_node, goal_node)
    edges = pf.extract_edges_from_path(path)

    if path:
        print(f"Shortest temporal path from {start_node} to {goal_node}: {path}")
    else:
        print(f"No path found from {start_node} to {goal_node}.")
    print(edges)