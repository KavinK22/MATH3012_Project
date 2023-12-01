import osmnx as ox
import networkx as nx
import numpy as np
import random
import time

graph = ox.graph_from_place('New York City, New York, USA', network_type='walk')
city_nodes, city_edges = ox.graph_to_gdfs(graph)

city_edges['test1'] = np.random.randint(1, 30000, city_edges.shape[0])
city_edges['test2'] = np.random.randint(200, 75000, city_edges.shape[0])


print(graph)
for _ in range(50):
    t0 = time.time()
    length_path = nx.dijkstra_path(graph, source = list(graph.nodes)[0], target = random.choice(list(graph.nodes)[1:]), weight = 'length')
    t = time.time()
    print(t-t0)
