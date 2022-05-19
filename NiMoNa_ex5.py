

import numpy as np
from matplotlib import pyplot as plt
from NiMoNa import *

def main(steps=200, dim=4):

    # initializing needed Parameters
    x = np.linspace(0, steps, steps)
    V = gen_V(c=1, rw=True, osc=[[1, 2], [np.pi/2, np.pi/2], [0, 0]], x=np.arange(10), dim=2)
    #print("{0}\n\n{1}".format(random_walk(steps=steps, dim=dim), np.cumsum(random_walk(steps=steps, dim=dim))))
    P = pop_development(C=1.5, V=V, steps=steps, dim=dim) #np.cumsum(random_walk(steps, dim), axis=1), x=x, P_0=np.array([0.5, 0.5])
    
    fig, axs = plt.subplots(dim, sharex=True)

    for i in range(dim):
        #print(P[i, 0, :])
        axs[i].plot(x, P[i, 0, :])
        axs[i].plot(x, P[i, 1, :])
    
    #plt.plot(x, P[0, 0, :], x, P[0, 1, :])
    plt.show()


if __name__ == "__main__":
    print(gen_C(c=1, rw=True, osc=[[1, 2], [np.pi/2, np.pi/2], [0, 0]], x=np.arange(10), dim=2))
    #main()
    