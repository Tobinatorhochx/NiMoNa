import networkx as nx
from matplotlib import pyplot as plt
import numpy as np
# current problem: doesn´t take "attr1" as argument

G = nx.random_geometric_graph(4, 0.5, dim=2)
G = nx.DiGraph(G)


node_v0 = {d: {"attr1":p0} for d, p0 in zip(np.arange(len(G.nodes())), np.ones(4)*0.5)}
nx.set_node_attributes(G, node_v0)

#edge_v0 = {(d, d+1): {"attr1":p0} for d, p0 in zip(np.arange(3), np.array([0.3, 0.9, 0.4, 1.2]))}
edge_v0 = {t:{"attr1":v} for t, v in zip(G.edges(), np.arange(len(G.edges())))}

nx.set_edge_attributes(G, edge_v0)



nlabels = nx.get_node_attributes(G, "attr1")
elabels = nx.get_edge_attributes(G, "attr1")

pos = nx.spring_layout(G)
#labels = nx.get_edge_data(G)

print(nx.to_numpy_array(G, weight="attr1"))
nx.draw(G, pos)


nx.draw_networkx_labels(G, pos, labels=nlabels)
nx.draw_networkx_edge_labels(G, pos, edge_labels=elabels)



plt.show()