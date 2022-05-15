# This exercise went pretty wild. The behaviour for A = 1 is cool, but things are starting to get nasty for bigger A. I only 
# decided to increase A by increments of 2, but I am still reaching populations below 0. I am not sure whether this is my bad 
# implementation of the model, or the model itself that leads to weird results.

# update #1: I changed the value of A, and it seems to have somewhat improved the results.

import numpy as np
import matplotlib.pyplot as plt


# r returns the replicator
def r(x, M):
    return M.dot(x)/np.dot(x, M.dot(x))
"""
# m returns an array containing the matrices for each set of parameters and time
def m(V, C, x, A):
    M = np.empty((2, 2, len(x), len(V)), dtype=float)
    for d, v, c, a in zip(np.arange(len(V)), V, C, A):
        for t  in range(len(x)):
            M[0, 0, t, d] = (v(x[t], a)-c)/2
            M[0, 1, t, d] = v(x[t], a)
            M[1, 0, t, d] = 0
            M[1, 1, t, d] = v(x[t], a)/2
        print("A: {0}, M: {1}\n\n".format(A, M))
    return M


def main(dim=5):

    # intitializing the parameters. C is constant, V fluctuating, p contains the populations and M are the matrices.
    C = [1.5 for x in range(dim)]
    V = [(lambda t, A: 1 + A * 0.1 * np.sin(t)) for x in range(dim)]
    A = [x/10 for x in range(1, 10*len(V), 10)]
    # first version: A = [x for x in range(1, 2*len(V), 2)]
    x = np.linspace(0, 15, 16)
    p = np.empty((dim, 2, 16))
    M = m(V, C, x, A)

    fig, axs = plt.subplots(dim, sharex=True)

    # calculating p
    for d in range(dim):
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

"""

def m(M, v, C):
    #print(M)
    for i in range(len(v)-1):
        
        M[i, 0, 0] = (v[i]- C)/2
        M[i, 0, 1] = v[i]
        M[i, 1, 0] = 0
        M[i, 1, 1] = v[i]/2
    return M

def main(dim=3):
    A = [0.1, 1, 10]
    C = 1.5
    f = [np.pi/2, np.pi/2, np.pi/2]
    x = np.linspace(0, 14, 15)
    V_x = np.empty((3, 15))
    V = lambda A, x, f: 1 + A * np.sin(f*x)
    Mat = np.empty((15, 2, 2), dtype=float)
    P = np.empty((dim, 2, 15))
    P[:, :, 0] = np.array([0.5, 0.5])

    for i in range(dim):
        V_x[i] = V(A=A[i], x=x, f=f[i])

    fig, axs = plt.subplots(dim, sharex=True)

    for j in range(dim):
        Matrix = m(M=Mat, v=V_x[j], C=C)
        print(Matrix)
        for k in range(len(x)-1):
            P[j, :, k+1] = P[j, :, k] * r(P[j, :, k], Matrix[k,:,:])

            P[j, :, k+1] =  P[j, :, k+1]/(sum(np.absolute(P[j, :, k+1]))) 
        axs[j].plot(x, P[j, 0, :])
        axs[j].plot(x, P[j, 1, :])
    plt.show()
    








if __name__ == "__main__":
    main()