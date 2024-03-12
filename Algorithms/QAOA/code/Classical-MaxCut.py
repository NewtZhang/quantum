import math
import time
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

sum_time = 0.0

start_time = time.perf_counter()

n = 6  # Number of nodes in graph
G = nx.Graph()
G.add_nodes_from(np.arange(0, n, 1))

elist = [(0, 2, 1.0), (0, 4, 1.0), (0, 5, 1.0), (1, 4, 1.0), (3, 4, 1.0),(0, 3, 1.0),
        (1, 5, 1.0), (2, 3, 1.0), (2, 4, 1.0), (2, 5, 1.0), (1, 3, 1.0),(0, 1, 1.0)]

# tuple is (i,j,weight) where (i,j) is the edge
G.add_weighted_edges_from(elist)

colors = ["r" for node in G.nodes()]
pos = nx.spring_layout(G)


def draw_graph(G, colors, pos):
    default_axes = plt.axes(frameon=True)
    nx.draw_networkx(G, node_color=colors, node_size=600, alpha=0.8, ax=default_axes, pos=pos)
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels)


draw_graph(G, colors, pos)

# Computing the weight matrix from the random graph
w = np.zeros([n, n])
for i in range(n):
    for j in range(n):
        temp = G.get_edge_data(i, j, default=0)
        if temp != 0:
            w[i, j] = temp["weight"]
print(w)

best_cost_brute = 0
for b in range(2**n):
    x = [int(t) for t in reversed(list(bin(b)[2:].zfill(n)))]
    cost = 0
    for i in range(n):
        for j in range(n):
            cost = cost + w[i, j] * x[i] * (1 - x[j])
    if best_cost_brute < cost:
        best_cost_brute = cost
        xbest_brute = x
    print("case = " + str(x) + " cost = " + str(cost))

colors = ["r" if xbest_brute[i] == 0 else "c" for i in range(n)]
draw_graph(G, colors, pos)
print("\nBest solution = " + str(xbest_brute) + " cost = " + str(best_cost_brute))

end_time = time.perf_counter()
elapsed_time = end_time - start_time

#print(f"Elapsed time: {elapsed_time:.6f} seconds")
sum_time += elapsed_time

print(f"Average time: {sum_time/1:.6f} seconds")
