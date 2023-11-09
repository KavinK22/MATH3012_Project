from MATH3012_Project_Graph_Class import Temporal_Spatial_Graph
import networkx as nx
import time
import random
class dijkstra:
    def __init__(self, graph):
        self.graph = graph
    #Dijkstra's Algorithm
    def dijkstra_temporal_with_path(self, start_node):
        start_time = time.time()
        shortest_paths = nx.single_source_dijkstra_path(self.graph.graph, source=start_node, weight='temporal_length')
        end_time = time.time()
        print(end_time-start_time)
        return shortest_paths

    def dijkstra_spatial_with_path(self, start_node):
        start_time = time.time()
        shortest_paths = nx.single_source_dijkstra_path(self.graph.graph, source=start_node, weight='spatial_length')
        end_time = time.time()
        print(end_time-start_time)
        return shortest_paths

    def extract_edges_from_path(self, path):
        if (len(path) == 1):
            return [2*path[0]]
        edges = []
        for i in range(len(path) - 1):
            edge = path[i] + path[i + 1]
            edges.append(edge)
        return edges
    
if __name__ == "__main__":
    # Example usage:
    my_graph = Temporal_Spatial_Graph()
    pf = dijkstra(my_graph)
    
    # for i in range(10):
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
    
    shortest_paths_temporal = pf.dijkstra_temporal_with_path(start_node)
    

    shortest_paths_spatial = pf.dijkstra_spatial_with_path(start_node)

    print(f"Shortest temporal paths from {start_node}:")
    for node, path in shortest_paths_temporal.items():
        print(f"time: {path}")
        edges = pf.extract_edges_from_path(path)
        print(f"To {node}: {edges}")

    print(f"\nShortest spatial paths from {start_node}:")
    for node, path in shortest_paths_spatial.items():
        print(path)
        edges = pf.extract_edges_from_path(path)
        print(f"To {node}: {edges}")
    