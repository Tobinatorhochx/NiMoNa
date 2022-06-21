from matplotlib import pyplot as plt
import numpy as np
import random


<<<<<<< HEAD
=======
#tasks: replace the random values in the edges with the correct values according to the migration policy

>>>>>>> master

class Network():
    def __init__(self, n, x, y, p_0):
        self.x = x
        self.y = y
        self.num = n
        self.pop = p_0
        



    def edgeofhawks(self, ListOfNodes):
            
            self.hawkedges = {(self.num, m):np.sqrt((self.x - snode.x)**2 + (self.y - snode.y)**2) * random.random() for snode, m in zip(ListOfNodes, range(len(ListOfNodes))) if self != snode}
            #print("{0}\n\n".format(self.edges))

    def edgeofdoves(self, ListOfNodes):
            
            self.doveedges = {(self.num, m):np.sqrt((self.x - snode.x)**2 + (self.y - snode.y)**2) * random.random()*2 for snode, m in zip(ListOfNodes, range(len(ListOfNodes))) if self != snode}
    

def total_pop(ListofNodes):
    p = 0
    for node in ListofNodes:
        p += np.sum(node.pop)
    return p


def network_development(ListOfNodes):

    for n1 in ListOfNodes:
        n1.next_pop = n1.pop
        for n2 in ListOfNodes:
            if n1.num != n2.num:

                n1.next_pop[0] += n2.pop[0] * n1.hawkedges[(n1.num, n2.num)]
            
                n1.next_pop[1] += n2.pop[1] * n1.doveedges[(n1.num, n2.num)]
    for node in ListOfNodes:
        node.pop = node.next_pop
    # for node in ListOfNodes:
    #     node.pop = node.pop/total_pop(ListOfNodes)
    #     print(total_pop(ListOfNodes))
    # print("\n\n")


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
    
    for k in range(1, steps):
        ListOfNodes = []
        for j in range(nnodes):
            
            P[j, :, k] = P[j, :, k-1] * r(P[j, :, k-1], Matrix[j, k-1,:,:])
            ListOfNodes.append(Network(j, random.random(), random.random(), P[j, :, k]))
        
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
        print(P[:,:,k], np.sum(P[:,:,k]))
        print("\n\n")
    return P