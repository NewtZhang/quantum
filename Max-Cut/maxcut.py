import networkx as nx
import numpy as np
import itertools
from scipy.sparse import csr_matrix

# 创建一个无向图
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4, 5])
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5)])

# 构建邻接矩阵
A = nx.adjacency_matrix(G)
n = A.shape[0]

# 将邻接矩阵转换为稀疏矩阵
A = csr_matrix(A)

# 定义目标函数
def objective_function(x):
    return x.dot(A.dot(1 - x))

# 枚举所有可能的割集
max_cut_value = 0
max_cut = None
for i in range(1, n // 2 + 1):
    for subset in itertools.combinations(range(n), i):
        x = np.zeros(n)
        x[list(subset)] = 1
        cut_value = objective_function(x)
        if cut_value > max_cut_value:
            max_cut_value = cut_value
            max_cut = subset

print("最大割集：", max_cut)
print("最大割值：", max_cut_value)