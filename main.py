
from matplotlib import pyplot as plt
import numpy as np
import random
import NiMoNa as nmn

#next idea: create dictionaries for each node containing the neighboring node and the edge value


         
        
nnodes = 4
steps = 15
P_0 = np.array([[0.1, 0.9],
                [0.5, 0.5],
                [0.1, 0.9],
                [0.3, 0.7]])

P = nmn.pop_development(C=nmn.gen_C(c=1, x=steps, dim=nnodes), V=nmn.gen_V(c=1.5, rw=True, osc=[[2, 2, 2, 2], [np.pi/2, np.pi/2, np.pi/2, np.pi/2], [0,0 ,0 ,0]], x=steps, dim=nnodes), P_0=P_0, steps=steps, nnodes=nnodes)



fig, axs = plt.subplots(nnodes, sharex=True)

for i in range(nnodes):
        
    axs[i].plot(np.arange(steps), P[i, 0, :], label="hawks")
    axs[i].plot(np.arange(steps), P[i, 1, :], label="doves")
axs[0].legend(loc="upper right")
plt.show()







