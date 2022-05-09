
import numpy as np
import matplotlib.pyplot as plt
# r returns the replicator
def r(x, M):
    #print(M)
    #print(M.dot(x), x)
    return M.dot(x)/np.dot(x, M.dot(x))

def m(V, C, x):
    M = np.empty((2, 2, len(x), len(V)))
    for d, v, c, A in zip(np.arange(len(V)), V, C, [x for x in range(1, 2*len(V), 2)]):
        for t  in range(len(x)):
            print(v(x[t], A))
            M[0, 0, t, d] = (v(x[t], A)-c)/2
            M[0, 1, t, d] = v(x[t], A)
            M[1, 0, t, d] = 0
            M[1, 1, t, d] = v(x[t], A)/2
    return M


def main():

    # intitializing the parameters
    C = [1.5 for x in range(5)]
    V = [(lambda t, A: 1 + A * 0.1 * np.sin(t)) for x in range(5)]



    x = np.linspace(0, 15, 15)
    p = np.empty((5, 2, 15))
    fig, axs = plt.subplots(5, sharex=True)

    M = m(V, C, x)

    
    for d in range(len(V)):
        p[d, :, 0] = np.array([0.5, 0.5])
        for i in range(p.shape[2]-1):       
            p[d, :, i+1] = p[d, :, i] * r(x = p[d, :, i], M = M[:, :, i, d])
        axs[d].plot(x, p[d, 0], label="hawks")
        axs[d].plot(x, p[d, 1], label="doves")
    #print(p)
    plt.legend()
    plt.show()


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

