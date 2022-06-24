
from matplotlib import pyplot as plt
import numpy as np
import random
import network as nk
import replicator_dynamic as rd
#next idea: create dictionaries for each node containing the neighboring node and the edge value


         
        
nnodes = 4
steps = 150
P_0 = np.array([[0.1, 0.9],
                [0.5, 0.5],
                [0.1, 0.9],
                [0.3, 0.7]])

P = rd.pop_development(C=rd.gen_C(c=1, x=steps, dim=nnodes), V=rd.gen_V(c=1.5, rw=True, osc=[[2, 2, 2, 2], [np.pi/2, np.pi/2, np.pi/2, np.pi/2], [0,0 ,0 ,0]], x=steps, dim=nnodes), P_0=P_0, steps=steps, nnodes=nnodes)








