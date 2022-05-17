

import numpy as np
from matplotlib import pyplot as plt
from NiMoNa import *

def main(steps=200, dim=2):

    # initializing needed Parameters
    x = np.linspace(0, steps, steps)
    #print("{0}\n\n{1}".format(random_walk(steps=steps, dim=dim), np.cumsum(random_walk(steps=steps, dim=dim))))
    P = pop_development(C=1.5, V=np.cumsum(random_walk(steps, dim), axis=1), x=x, P_0=np.array([0.5, 0.5]), steps=steps, dim=dim)
    
    fig, axs = plt.subplots(dim, sharex=True)

    for i in range(dim):
        print(P[i, 0, :])
        axs[i].plot(x, P[i, 0, :])
        axs[i].plot(x, P[i, 1, :])
    
    #plt.plot(x, P[0, 0, :], x, P[0, 1, :])
    plt.show()


if __name__ == "__main__":
    main(steps=20)