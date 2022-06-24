from typing import List
import numpy as np
from network import Network, total_pop, network_development, draw_network
import random
import matplotlib.pyplot as plt


# parameter calculated by a random walk
def random_walk(steps, dim):   
    arr = np.empty((dim, steps))
    for i in range(dim):
        np.random.seed(i)
        arr[i] = np.array([np.random.normal(loc=0, scale=1) for x in range(steps)])
    return arr

# oscillating parameters
def oscillation(x, dim, amp, freq, phase):
    arr = np.empty((dim, x))
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
        rw = random_walk(x, dim)
    if osc != 0:
        osc = oscillation(x, dim, osc[0], osc[1], osc[2])
    c = np.ones((dim, x)) * c
    
    return c + osc + rw

# returns multidimensional array containing V
def gen_C(c=0, rw=0, osc=0, x=0, dim=0):
    if rw == True:
        rw = random_walk(len(x), dim)
    if osc != 0:
        osc = oscillation(x, dim, osc[0], osc[1], osc[2])
    c = np.ones((dim, x)) * c
    
    return c + osc + rw




# returns array containing the population
def pop_development(C, V, P_0, steps, nnodes):

    # initiating the population-array
    P = np.empty((nnodes, 2, steps))
    
    P[:, :, 0] = P_0/np.sum(P_0)

    # setting up the matrix
    Matrix = m(M=np.empty((nnodes, steps, 2, 2), dtype=float), v=V, C=C)
    ListOfNodes = [Network(j, random.random(), random.random(), P[j, :, 0]) for j in range(nnodes)]

    for k in range(1, steps):
        for j in range(nnodes):
            
            P[j, :, k] = P[j, :, k-1] * r(P[j, :, k-1], Matrix[j, k-1,:,:])
            ListOfNodes[j].pop = P[j, :, k]
            
        
        # setting up the Nodes and the connecting edges
        for node in ListOfNodes:
            node.edgeofhawks(ListOfNodes=ListOfNodes)
            node.edgeofdoves(ListOfNodes=ListOfNodes)
        #network effects
        network_development(ListOfNodes)

        for node in ListOfNodes:
            
            P[node.num, :, k] = node.pop

        #normalizing the population
        P[:,:,k] = P[:,:,k]/np.sum(P[:,:,k])
        # print(P[:,:,k], np.sum(P[:,:,k]))
        # print("\n\n")
    


    fig, axs = plt.subplots(nnodes, sharex=True)

    for i in range(nnodes):
        axs[i].plot(np.arange(steps), P[i, 0, :], label="hawks")
        axs[i].plot(np.arange(steps), P[i, 1, :], label="doves")
    axs[0].legend(loc="upper right")
    plt.show()

    draw_network(ListOfNodes=ListOfNodes)

    return 0