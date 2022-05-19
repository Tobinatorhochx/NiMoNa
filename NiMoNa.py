import numpy as np

from testing_ground import C

def random_walk(steps, dim):
    
    arr = np.empty((dim, steps))
    
    for i in range(dim):
        np.random.seed(i)
        arr[i] = np.array([np.random.normal(loc=0, scale=1) for x in range(steps)])
    return arr

def oscillation(x, dim, amp, freq, phase):

    arr = np.empty((dim, len(x)))
    F = lambda A, f, t, p: A * np.cos(f * t + p)
    for i in range(dim):
        arr[i] = F(amp[i], freq[i], x, phase[i])
    return arr



# r returns the replicator
def r(x, M):
    return M.dot(x)/np.dot(x, M.dot(x))

# m returns the matrix
def m(M, v, C):
    for i in range(len(v)-1):       
        M[i, 0, 0] = (v[i]- C[i])/2
        M[i, 0, 1] = v[i]
        M[i, 1, 0] = 0
        M[i, 1, 1] = v[i]/2

    return M


def gen_V(c=0, rw=0, osc=0, x=0, dim=0):
    if rw == True:
        rw = random_walk(len(x), dim)
    if osc != 0:
        osc = oscillation(x, dim, osc[0], osc[1], osc[2])
    c = np.ones((dim, len(x))) * c
    
    return c + osc + rw

def gen_C(c=0, rw=0, osc=0, x=0, dim=0):
    if rw == True:
        rw = random_walk(len(x), dim)
    if osc != 0:
        osc = oscillation(x, dim, osc[0], osc[1], osc[2])
    c = np.ones((dim, len(x))) * c
    
    return C + osc + rw


def pop_development(C, V, P_0, x, steps, dim):
    """ # The idea is to turn C and V into a multidimensional array, so that they can be used by the rest of the program.
    if type(C) == float or type(C) == int:
        C = np.array([[C for x in range(steps)] for y in range(dim)])
    if type(V) == float or type(V) == int:
        V = np.array([[V for x in range(steps)] for y in range(dim)])
    if V.shape != (dim, steps):
        V = np.array([V for x in range(dim)])
    if C.shape != (dim, steps):
        C = np.array([C for x in range(dim)])"""
    

    
    
    

    P = np.empty((dim, 2, steps))
    P[:, :, 0] = P_0
    

    for j in range(dim):
        
        Matrix = m(M=np.empty((steps, 2, 2), dtype=float), v=V[j], C=C[j])
            
        for k in range(len(x)-1):
            # calculating the next generation
            P[j, :, k+1] = P[j, :, k] * r(P[j, :, k], Matrix[k,:,:])
            # normalizing the population
            P[j, :, k+1] =  P[j, :, k+1]/(sum(np.absolute(P[j, :, k+1]))) 

    return P