# This exercise went pretty wild. The behaviour for A = 1 is cool, but things are starting to get nasty for bigger A. I only 
# decided to increase A by increments of 2, but I am still reaching populations below 0. I am not sure whether this is my bad 
# implementation of the model, or the model itself that leads to weird results.

# update #1: I changed the value of A, and it seems to have somewhat improved the results.


# update #2: restarted the whole project as I found out that my results where completely false

# update #3: added the missing exercises.


import numpy as np
import matplotlib.pyplot as plt
from scipy import rand


# r returns the replicator
def r(x, M):
    return M.dot(x)/np.dot(x, M.dot(x))

# m returns the matrix
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
    f = [1, np.pi/2, np.pi/2]
    x = np.linspace(0, 100, 100)
    V_x = np.empty((3, 100))
    V = lambda A, x, f: 1 + A * np.sin(f*x)
    Mat = np.empty((100, 2, 2), dtype=float)
    P = np.empty((dim, 2, 100))
    P[:, :, 0] = np.array([0.5, 0.5])

    for i in range(dim):
        V_x[i] = V(A=A[i], x=x, f=f[i])

    fig, axs = plt.subplots(dim, sharex=True)

    for j in range(dim):
        Matrix = m(M=Mat, v=V_x[j], C=C)
        print(Matrix)
        for k in range(len(x)-1):
            P[j, :, k+1] = P[j, :, k] * r(P[j, :, k], Matrix[k,:,:])
            # normalizing
            P[j, :, k+1] =  P[j, :, k+1]/(sum(np.absolute(P[j, :, k+1]))) 
        axs[j].plot(x, P[j, 0, :])
        axs[j].plot(x, P[j, 1, :])
        axs[j].set_title("V = 1 + {0}sin({1}x)".format(A[j],f[j]))
    plt.show()
    
def random_walk(steps, dim):
    
    
    
        
    arr = np.empty((dim, steps))
    for i in range(dim):
        np.random.seed(i)
        arr[i] = np.array([np.random.normal(loc=0, scale=1) for x in range(steps)])
        plt.plot(np.arange(steps), np.cumsum(arr[i]), label="seed = {0}, mean = {1}, standard-deviation = {2}".format(i, np.mean(np.cumsum(arr[i])), np.std(np.cumsum(arr[i]))))
    
    plt.legend()
    plt.show()
















if __name__ == "__main__":
   main()
   random_walk(100000, 3)