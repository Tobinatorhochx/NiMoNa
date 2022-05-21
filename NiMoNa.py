import numpy as np
import networkx as nx
import random as rnd

# parameter calculated by a random walk
def random_walk(steps, dim):   
    arr = np.empty((dim, steps))
    for i in range(dim):
        np.random.seed(i)
        arr[i] = np.array([np.random.normal(loc=0, scale=1) for x in range(steps)])
    return arr

# oscillating parameters
def oscillation(x, dim, amp, freq, phase):
    arr = np.empty((dim, len(x)))
    F = lambda A, f, t, p: A * np.cos(f * t + p)
    for i in range(dim):
        arr[i] = F(amp[i], freq[i], x, phase[i])
    return arr


# r returns the replicator
def r(x, M):
    return M.dot(x)/np.dot(x, M.dot(x))

# m returns the matrix
def m(M, v, C):
    for d in range(M.shape[0]):
        for i in range(M.shape[1]):       
            M[d, i, 0, 0] = (v[d, i]- C[d, i])/2
            M[d, i, 0, 1] = v[d, i]
            M[d, i, 1, 0] = 0
            M[d, i, 1, 1] = v[d, i]/2

    return M

# returns multidimensional array containing C
def gen_V(c=0, rw=0, osc=0, x=0, dim=0):
    if rw == True:
        rw = random_walk(len(x), dim)
    if osc != 0:
        osc = oscillation(x, dim, osc[0], osc[1], osc[2])
    c = np.ones((dim, len(x))) * c
    
    return c + osc + rw

# returns multidimensional array containing V
def gen_C(c=0, rw=0, osc=0, x=0, dim=0):
    if rw == True:
        rw = random_walk(len(x), dim)
    if osc != 0:
        osc = oscillation(x, dim, osc[0], osc[1], osc[2])
    c = np.ones((dim, len(x))) * c
    
    return c + osc + rw

# returns the updated populations after interaction between the nodes
def network_development(p, dim, G, G1):
    pops = np.empty(p.shape)

    for e in G.edges():
        pops[e[0]][0] = p[e[0]][0] + G[e[0]][e[1]]["value"] * p[e[1]][0]
        pops[e[1]][0] = p[e[1]][0] + G[e[1]][e[0]]["value"] * p[e[0]][0]
    for e in G1.edges():
        pops[e[0]][1] = p[e[0]][1] + G1[e[0]][e[1]]["value"] * p[e[1]][1]
        pops[e[1]][1] = p[e[1]][1] + G1[e[1]][e[0]]["value"] * p[e[0]][1]
    return pops
        



# returns array containing the population
def pop_development(C, V, P_0, x, node_factor, steps, dim):

    # initiating the population-array
    P = np.empty((dim, 2, steps))
    P[:, :, 0] = P_0

    # setting up the matrix
    Matrix = m(M=np.empty((dim, steps, 2, 2), dtype=float), v=V, C=C)
    

    # setting up the network
    G = nx.DiGraph()
    for i in range(dim):
        G.add_node(i)
    pos = nx.random_layout(G)
    for i in range(dim):
        for j in range(dim):
            if np.sqrt((pos[i][0]-pos[j][0])**2-(pos[i][1]-pos[i][1])**2) < 0.6 and i != j:
                G.add_edge(i, j)
    nodes_0 = {d:{"pop":p} for d, p in zip(range(dim), P[:, 0, 0])}
    nx.set_node_attributes(G, nodes_0)

    # G for the hawks, G1 for the doves
    G1 = G.copy() 

    for e in G.edges():
        # here is room for further implementations, e. g. greater migration in areas less suited for living
        G[e[0]][e[1]]["value"] = 1/(node_factor * np.sqrt(e[0]**2 + e[1]**2) - rnd.gauss(0, 0.5))

    for e in G1.edges():
        G1[e[0]][e[1]]["value"] = 1/(node_factor * np.sqrt(e[0]**2 + e[1]**2) - rnd.gauss(0, 0.5))

    
    for k in range(len(x)-1):    
        for j in range(dim):

            # calculating the next generation
            P[j, :, k+1] = P[j, :, k] * r(P[j, :, k], Matrix[j, k,:,:])
        # interactions with the network
        P[:, :, k+1] = network_development(P[:, :, k], dim=dim, G=G, G1=G1)
        
            
        # normalizing the population
        for j in range(dim):
            P[j, :, k+1] =  P[j, :, k+1]/(sum(np.absolute(P[j, :, k+1]))) 

    return P, G, G1, pos