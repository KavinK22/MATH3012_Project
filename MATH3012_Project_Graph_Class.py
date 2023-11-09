import networkx as nx

class TemporalSpatialGraph:
    def __init__(self):
        self.graph = nx.Graph()
        self.node_count = 0

    def add_node(self):
        node_name = f"p{self.node_count}"
        self.graph.add_node(node_name)
        self.node_count += 1

    def add_edge(self, node1, node2, temporal_length, spatial_length):
        self.graph.add_edge(node1, node2, temporal_length=temporal_length, spatial_length=spatial_length)

    def dijkstra_temporal(self, start_node):
        distances_temporal = nx.single_source_dijkstra_path_length(self.graph, start_node, weight='temporal_length')
        return distances_temporal

    def dijkstra_spatial(self, start_node):
        distances_spatial = nx.single_source_dijkstra_path_length(self.graph, start_node, weight='spatial_length')
        return distances_spatial

    def __str__(self):
        return str(self.graph)

if __name__ == "__main__":
    # Example usage:
    my_graph = TemporalSpatialGraph()

    my_graph.add_node()
    my_graph.add_node()
    my_graph.add_node()

    my_graph.add_edge("p0", "p1", temporal_length=10, spatial_length=2.5)
    my_graph.add_edge("p1", "p2", temporal_length=15, spatial_length=3.0)

    start_node = "p0"
    distances_temporal = my_graph.dijkstra_temporal(start_node)
    distances_spatial = my_graph.dijkstra_spatial(start_node)

    print(f"Shortest temporal distances from {start_node}:")
    for node, distance in distances_temporal.items():
        print(f"To {node}: {distance}")

    print(f"\nShortest spatial distances from {start_node}:")
    for node, distance in distances_spatial.items():
        print(f"To {node}: {distance}")
