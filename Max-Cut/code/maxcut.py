# useful additional packages
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import time

# from qiskit_aer import Aer
# from qiskit.tools.visualization import plot_histogram
# from qiskit.circuit.library import TwoLocal
# from qiskit_optimization.applications import Maxcut, Tsp
# from qiskit.algorithms.minimum_eigensolvers import SamplingVQE, NumPyMinimumEigensolver
# from qiskit.algorithms.optimizers import SPSA
# from qiskit.utils import algorithm_globals
# from qiskit.primitives import Sampler
# from qiskit_optimization.algorithms import MinimumEigenOptimizer


# sum_time = 0.0
# for i in range(10): 
#     start_time = time.perf_counter()

#     # Generating a graph of 4 nodes

#     n = 15  # Number of nodes in graph
#     G = nx.Graph()
#     G.add_nodes_from(np.arange(0, n, 1))
#     elist = [(0, 2, 1.0), (0, 3, 1.0), (0, 4, 1.0), (0, 5, 1.0), (0, 9, 1.0), (1, 3, 1.0), (1, 4, 1.0), (1, 5, 1.0), 
#             (2, 3, 1.0), (2, 4, 1.0), (2, 6, 1.0), (2, 7, 1.0), (4, 5, 1.0), (4, 6, 1.0), (5, 8, 1.0), (5, 9, 1.0), 
#             (6, 7, 1.0), (6, 8, 1.0), (6, 9, 1.0), (7, 8, 1.0), (7, 10, 1.0), (7, 14, 1.0), (8, 12, 1.0), (8, 13, 1.0), 
#             (8, 14, 1.0), (9, 10, 1.0), (9, 11, 1.0), (9, 13, 1.0), (10, 12, 1.0), (10, 13, 1.0), (10, 14, 1.0), (11, 13, 1.0), 
#             (12, 13, 1.0), (12, 14, 1.0), (13, 14, 1.0)]
#     # tuple is (i,j,weight) where (i,j) is the edge
#     G.add_weighted_edges_from(elist)

#     colors = ["r" for node in G.nodes()]
#     pos = nx.spring_layout(G)


#     def draw_graph(G, colors, pos):
#         default_axes = plt.axes(frameon=True)
#         nx.draw_networkx(G, node_color=colors, node_size=600, alpha=0.8, ax=default_axes, pos=pos)
#         edge_labels = nx.get_edge_attributes(G, "weight")
#         nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels)


#     draw_graph(G, colors, pos)

#     # Computing the weight matrix from the random graph
#     w = np.zeros([n, n])
#     for i in range(n):
#         for j in range(n):
#             temp = G.get_edge_data(i, j, default=0)
#             if temp != 0:
#                 w[i, j] = temp["weight"]
#     print(w)

#     best_cost_brute = 0
#     for b in range(2**n):
#         x = [int(t) for t in reversed(list(bin(b)[2:].zfill(n)))]
#         cost = 0
#         for i in range(n):
#             for j in range(n):
#                 cost = cost + w[i, j] * x[i] * (1 - x[j])
#         if best_cost_brute < cost:
#             best_cost_brute = cost
#             xbest_brute = x
#         print("case = " + str(x) + " cost = " + str(cost))

#     colors = ["r" if xbest_brute[i] == 0 else "c" for i in range(n)]
#     draw_graph(G, colors, pos)
#     print("\nBest solution = " + str(xbest_brute) + " cost = " + str(best_cost_brute))

#     end_time = time.perf_counter()
#     elapsed_time = end_time - start_time

#     #print(f"Elapsed time: {elapsed_time:.6f} seconds")
#     sum_time += elapsed_time

# print(f"Average time: {sum_time/10:.6f} seconds")

















start_time = time.perf_counter()

# Generating a graph of 4 nodes

n = 15  # Number of nodes in graph
G = nx.Graph()
G.add_nodes_from(np.arange(0, n, 1))
elist = [(0, 2, 1.0), (0, 3, 1.0), (0, 4, 1.0), (0, 5, 1.0), (0, 9, 1.0), (1, 3, 1.0), (1, 4, 1.0), (1, 5, 1.0), 
        (2, 3, 1.0), (2, 4, 1.0), (2, 6, 1.0), (2, 7, 1.0), (4, 5, 1.0), (4, 6, 1.0), (5, 8, 1.0), (5, 9, 1.0), 
        (6, 7, 1.0), (6, 8, 1.0), (6, 9, 1.0), (7, 8, 1.0), (7, 10, 1.0), (7, 14, 1.0), (8, 12, 1.0), (8, 13, 1.0), 
        (8, 14, 1.0), (9, 10, 1.0), (9, 11, 1.0), (9, 13, 1.0), (10, 12, 1.0), (10, 13, 1.0), (10, 14, 1.0), (11, 13, 1.0), 
        (12, 13, 1.0), (12, 14, 1.0), (13, 14, 1.0)]
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