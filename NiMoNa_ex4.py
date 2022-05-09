# This exercise went pretty wild. The behaviour for A = 1 is cool, but things are starting to get nasty for bigger A. I only 
# decided to increase A by increments of 2, but I am still reaching populations below 0. I am not sure whether this is my bad 
# implementation of the model, or the model itself that leads to weird results.


import numpy as np
import matplotlib.pyplot as plt


# r returns the replicator
def r(x, M):
    return M.dot(x)/np.dot(x, M.dot(x))

# m returns an array containing the matrices for each set of parameters and time
def m(V, C, x, A):
    M = np.empty((2, 2, len(x), len(V)))
    for d, v, c, a in zip(np.arange(len(V)), V, C, A):
        for t  in range(len(x)):
            M[0, 0, t, d] = (v(x[t], a)-c)/2
            M[0, 1, t, d] = v(x[t], a)
            M[1, 0, t, d] = 0
            M[1, 1, t, d] = v(x[t], a)/2
    return M


def main():

    # intitializing the parameters. C is constant, V fluctuating, p contains the populations and M are the matrices.
    C = [1.5 for x in range(5)]
    V = [(lambda t, A: 1 + A * 0.1 * np.sin(t)) for x in range(5)]
    A = [x for x in range(1, 2*len(V), 2)]
    x = np.linspace(0, 15, 16)
    p = np.empty((5, 2, 16))
    M = m(V, C, x, A)

    fig, axs = plt.subplots(5, sharex=True)

    # calculating p
    for d in range(len(V)):
        p[d, :, 0] = np.array([0.5, 0.5])
        for i in range(p.shape[2]-1):       
            p[d, :, i+1] = p[d, :, i] * r(x = p[d, :, i], M = M[:, :, i, d])            
            # normalizing the population
            p[d, :, i+1] =  p[d, :, i+1]/(sum(np.absolute(p[d, :, i+1]))) 

    # plotting the populations
        axs[d].plot(x, p[d, 0], label="hawks")
        axs[d].plot(x, p[d, 1], label="doves")
        axs[d].set_title("V = 1 + A * sin(x), C = {0}, A = {1}".format(C[d], A[d]))
    axs[0].legend(loc="upper right")
    axs[0].set_ylim([0,1])  
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()


"""

    for V, C, p_0, p_1, d in [[1., 1.5, 0.5, 0.5, 0],[1.5, 1., 0.5, 0.5, 1],[1., 1.5, 0.1, 0.9, 2],[1., 1.5, 0.9, 0.1, 3]]:
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
    
    
    x = np.linspace(0, 15, 400)
    y = np.sin(40*x)
    axs[4].plot(x, y)
    plt.show()
"""

