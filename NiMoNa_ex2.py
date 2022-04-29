#I hope that everything works as intended. It can´t be seen that good, but for V > C, the population of the
#hawks is reaching 1. If V < C, a stable state is formed where both species coexist.

# I did not have the time to add oscillating values for V and C, but I might return to it later.


import numpy as np
import matplotlib.pyplot as plt

# r returns the replicator
def r(x, M):
    return M.dot(x)/np.dot(x, M.dot(x))

def main():

    # intitializing the parameters

    
    x = np.linspace(0, 15, 15)
    p = np.empty((4, 2, 15))
    fig, axs = plt.subplots(4, sharex=True)

    for V, C, p_0, p_1, d in [[1, 1.5, 0.5, 0.5, 0],[1.5, 1, 0.5, 0.5, 1],[1, 1.5, 0.1, 0.9, 2],[1, 1.5, 0.9, 0.1, 3]]:
        # Payoff matrix
        M = np.array([[(V-C)/2, V], [0,V/2]])
        # storing the population in a 3D-array
        p[d, 0:2, 0] = np.array([p_0, p_1])
        for i in range(p.shape[2]-1):
            p[d, 0:2, i+1] = p[d, 0:2, i] * r(x = p[d, 0:2, i], M = M)
    
    # plotting the function and adjusting parameters
        axs[d].plot(x, p[d, 0], label = "Hawks") 
        axs[d].plot(x, p[d, 1], label = "Doves")
        axs[d].set_title("V = {0}, C = {1}, P_0 = {2} = {3}".format(V, C, p_0, p_1))
    axs[0].legend(loc="upper right")
    axs[0].set_ylim([0,1])
    axs[2].set_ylim([0,1])
    plt.tight_layout()
    plt.show()


main()


#