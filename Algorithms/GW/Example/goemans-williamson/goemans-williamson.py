import cvxpy as cp
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import scipy.linalg

#for commented QAOA
from qiskit_aer import Aer
from qiskit.tools.visualization import plot_histogram
from qiskit.circuit.library import TwoLocal
from qiskit_optimization.applications import Maxcut, Tsp
from qiskit.algorithms.minimum_eigensolvers import SamplingVQE, NumPyMinimumEigensolver
from qiskit.algorithms.optimizers import SPSA
from qiskit.utils import algorithm_globals
from qiskit.primitives import Sampler
from qiskit_optimization.algorithms import MinimumEigenOptimizer




def draw_graph(G, colors, pos):
    default_axes = plt.axes(frameon=True)
    nx.draw_networkx(G, node_color=colors, node_size=400, alpha=0.8, ax=default_axes, pos=pos)
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels)
    plt.show()

#CLASSICAL
n = 5
G = nx.Graph()
G.add_nodes_from(np.arange(0,4,1))


edges = [(1,2),(1,3),(2,4),(3,4),(3,0),(4,0)]
#edges = [(0,1),(1,2),(2,3),(3,4)]#[(1,2),(2,3),(3,4),(4,5)]
G.add_edges_from(edges)

#colors = ["g" for node in G.nodes()]
pos = nx.spring_layout(G)
#draw_graph(G, colors, pos)
w = np.zeros([n, n])
for i in range(n):
    for j in range(n):
        temp = G.get_edge_data(i, j, default=0)
        if temp != 0:
            w[i, j] = 1



#Goemans-Williamson 0.87
X = cp.Variable((n,n), symmetric = True) #construct nxn matrix
constraints = [X >> 0] + [ X[i,i] == 1 for i in range(n) ]
# diagonals must be 1 (unit) and eigenvalues must be postivie
#semidefinite


objective = sum( (0.5)* (1 - X[i,j]) for (i,j) in edges) 
#this is function defing the cost of the cut. You want to maximize this function
#to get heaviest cut

prob = cp.Problem(cp.Maximize(objective), constraints)
prob.solve()
#solves semidefinite program, optimizes linear cost function

sqrtProb = scipy.linalg.sqrtm(X.value)
#normalizes matrix, makes it applicable in unit sphere

hyperplane = np.random.randn(n)
#generates random hyperplane used to split set of points into two disjoint sets of nodes

sqrtProb = np.sign( sqrtProb @ hyperplane)
#gives value -1 if on one side of plane and 1 if on other
#returned as a array

print(sqrtProb)


colors = ["r" if sqrtProb[i] == -1 else "c" for i in range(n)]
sets = [0 if sqrtProb[i] == -1 else 1 for i in range(n)]




draw_graph(G, colors, pos)
print("\Approximated solution = " + str(sets))

''' #Naive Solution NP

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
'''


#QUANTUM
'''
max_cut = Maxcut(w)
qp = max_cut.to_quadratic_program()
print(qp.prettyprint())

qubitOp, offset = qp.to_ising()
print("Offset:", offset)
print("Ising Hamiltonian:")
print(str(qubitOp))

# solving Quadratic Program using exact classical eigensolver
exact = MinimumEigenOptimizer(NumPyMinimumEigensolver())
result = exact.solve(qp)
print(result.prettyprint())

# Making the Hamiltonian in its full form and getting the lowest eigenvalue and eigenvector
ee = NumPyMinimumEigensolver()
result = ee.compute_minimum_eigenvalue(qubitOp)

x = max_cut.sample_most_likely(result.eigenstate)
print("energy:", result.eigenvalue.real)
print("max-cut objective:", result.eigenvalue.real + offset)
print("solution:", x)
print("solution objective:", qp.objective.evaluate(x))

colors = ["r" if x[i] == 0 else "c" for i in range(n)]
draw_graph(G, colors, pos)

algorithm_globals.random_seed = 123
seed = 10598

# construct SamplingVQE
optimizer = SPSA(maxiter=300)
ry = TwoLocal(qubitOp.num_qubits, "ry", "cz", reps=5, entanglement="linear")
vqe = SamplingVQE(sampler=Sampler(), ansatz=ry, optimizer=optimizer)

# run SamplingVQE
result = vqe.compute_minimum_eigenvalue(qubitOp)

# print results
x = max_cut.sample_most_likely(result.eigenstate)
print("energy:", result.eigenvalue.real)
print("time:", result.optimizer_time)
print("max-cut objective:", result.eigenvalue.real + offset)
print("solution:", x)
print("solution objective:", qp.objective.evaluate(x))

# plot results
colors = ["r" if x[i] == 0 else "c" for i in range(n)]
draw_graph(G, colors, pos)

# create minimum eigen optimizer based on SamplingVQE
vqe_optimizer = MinimumEigenOptimizer(vqe)

# solve quadratic program
result = vqe_optimizer.solve(qp)
print(result.prettyprint())

colors = ["r" if result.x[i] == 0 else "c" for i in range(n)]
draw_graph(G, colors, pos)
'''
