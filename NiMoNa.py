import numpy as np


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

# returns multidimensional array containing C
def gen_V(c=0, rw=0, osc=0, x=0, dim=0):
    if rw == True:
        rw = random_walk(len(x), dim)
    if osc != 0:
        osc = oscillation(x, dim, osc[0], osc[1], osc[2])
    c = np.ones((dim, len(x))) * c
    
    return c + osc + rw

# returns multidimensional array containing V
def gen_C(c=0, rw=0, osc=0, x=0, dim=0):
    if rw == True:
        rw = random_walk(len(x), dim)
    if osc != 0:
        osc = oscillation(x, dim, osc[0], osc[1], osc[2])
    c = np.ones((dim, len(x))) * c
    
    return c + osc + rw


#def network_development()



# returns array containing the population
def pop_development(C, V, P_0, x, steps, dim):
    
    # initiating the population-array
    P = np.empty((dim, 2, steps))
    
    P[:, :, 0] = P_0
    

    for j in range(dim):
        #P[j, :, 0] = P_0[j]
        # setting up the matrix
        Matrix = m(M=np.empty((steps, 2, 2), dtype=float), v=V[j], C=C[j])
            
        for k in range(len(x)-1):
            # calculating the next generation
            P[j, :, k+1] = P[j, :, k] * r(P[j, :, k], Matrix[k,:,:])
            # normalizing the population
            P[j, :, k+1] =  P[j, :, k+1]/(sum(np.absolute(P[j, :, k+1]))) 

    return P



class Population():

    def __init__(self):
        self.x , self.y = np.random.uniform(0, 1), np.random.uniform(0, 1)
