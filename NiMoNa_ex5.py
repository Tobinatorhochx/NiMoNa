# This is the current version of the fifth exercise. As the code got pretty messy, I will outline the general idea and current problems here:
# Changes between this and the fourth exercise:
#   - added additional parameters to the payoff V and the cost C
#   - added a first version of a depiction of the graph network

# general idea: 
# The graph should initiate a directed graph with nodes at random positions and edges between nodes which are somewhat close to each other (determination by geometric distance).
# The value on the edges should represent the parameter, with which population in node i is increased by multiplication of node j with the edge-value.
# This edge value consists of a constant multiplicative factor, a random constant and depends on the distance between two nodes.
# Between each steps, the population of each node is first multiplied by the replicator and then changes depending on the graph network.

# conclusions so far:
#   - adding the networks most often leads to a asymptotic alignment of the values in each population. There are exceptions to that depending on
#     the random constant between the edges, but this is rare.
#   - without the network, fluctuations within the populations are quite wild. With the network, the changes "even out" and lead to a smooth
#     approximation of a limit

# problems:
#   - the nodes in the graph are somehow not at random positions. This might be, I have defined a seed and networkx might use this seed for position-generation
#   - there must be an issue with node-generation, as it looks like this is an undirected graph
#   - there is not much variation in the way the edges are 

#documentation: nmn.gen_C(c = const., rw=True/False, ocs=[[Amplitude],[Frequency],[Phase shift]] , x=array, dim=int)
import numpy as np
from matplotlib import pyplot as plt
import NiMoNa_networkx as nmn
import networkx as nx

def main(steps=200, dim=4):



    # initializing needed Parameters
    x = np.linspace(0, steps, 10*steps)
    background_fitness = [0, 0, 0, 0]
    c_C, c_V= 1.5, 1.5
    P_0 = np.array([[0.5, 0.5], [0.6, 0.4], [0.1, 0.9], [0.35, 0.65]])
    osc_V = [[1, 2, 4, 4], [1, 0.1, 3, 3], [0, 0, 0, 0]]
    V = nmn.gen_V(c=c_V, rw=False, osc=osc_V, x=x, dim=dim)#
    osc_C = [[0.1, 1, 100, 100], [0.1*np.pi/2, np.pi/2, 100*np.pi/2, 100*np.pi/2], [0, 0, np.pi/4, np.pi/4]]
    C = nmn.gen_C(c=c_C, rw=True, osc=osc_C,  x=x, dim=dim) #
    P , G, G1, pos= nmn.pop_development(C=C, x=x, P_0=P_0, V=V, background_fitness=background_fitness, node_factor = 1, steps=steps, dim=dim)
    nodes_hawks = {d:{"pop":p} for d, p in zip(range(dim), P[:, 0, -1])}
    
    nodes_doves = {d:{"pop":p} for d, p in zip(range(dim), P[:, 1, -1])}
    nx.set_node_attributes(G, nodes_hawks)

    # plotting the first diagrams

    fig, axs = plt.subplots(dim, sharex=True)

    for i in range(dim):
        
        axs[i].plot(x, P[i, 0, :], label="hawks")
        axs[i].plot(x, P[i, 1, :], label="doves")
        axs[i].set_title("P: const. = {0}, Amplitude= {1}, Frequenz = {2}, phase = {3}; C: const. = {4}, Amplitude= {5}, Frequenz = {6}, phase = {7}".format(c_V, osc_V[0][i], osc_V[1][i], osc_V[2][i], c_C, osc_C[0][i], osc_C[1][i], osc_C[2][i]))
    axs[0].legend(loc="upper right")
    plt.show()

    # plotting the graph network

    plt.figure()
    plt.title("Graph network depicting the relative populations of the hawks")

    nlabels = nx.get_node_attributes(G, "pop")
    elabels = nx.get_edge_attributes(G, "value")

    nx.draw_networkx_nodes(G, pos=pos)
    nx.draw_networkx_edges(G, pos=pos, connectionstyle='arc3, rad = 0.1')
    nx.draw_networkx_labels(G, pos, labels=nlabels)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=elabels, font_size=5)
    plt.show()

    
if __name__ == "__main__":   
    main()
    