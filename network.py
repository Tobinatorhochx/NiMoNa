from typing import List
import numpy as np
import random
import matplotlib.pyplot as plt



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
    


def draw_network(ListOfNodes):
        plt.axis("off")
        x_arr = np.array([node.x for node in ListOfNodes])
        y_arr = np.array([node.y for node in ListOfNodes])
        v_arr = np.array([node.pop[0] for node in ListOfNodes])

        plt.scatter(x_arr, y_arr, c=v_arr, cmap="gray")
        
        plt.show()
            

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
