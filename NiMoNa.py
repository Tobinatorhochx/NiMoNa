import numpy as np

def random_walk(steps, dim):
    
    
    
        
    arr = np.empty((dim, steps))
    for i in range(dim):
        np.random.seed(i)
        arr[i] = np.array([np.random.normal(loc=0, scale=1) for x in range(steps)])
        
    return arr

# r returns the replicator
def r(x, M):
    return M.dot(x)/np.dot(x, M.dot(x))

# m returns the matrix
def m(M, v, C):
    


    for i in range(len(v)-1):
        
        M[i, 0, 0] = (v[i]- C)/2
        M[i, 0, 1] = v[i]
        M[i, 1, 0] = 0
        M[i, 1, 1] = v[i]/2
    return M



def pop_development(C, V, P_0, steps, dim):
    if C == float or C == int:
        C = np.array([C for x in range(steps)]).concatenate((dim, steps))
    if V == float or V == int:
        V = np.array([V for x in range(steps)]).concatenate((dim, steps))


    x = np.linspace(0, steps, steps+1)
    
    
    Mat = np.empty((steps, 2, 2), dtype=float)
    P = np.empty((dim, 2, steps))
    P[:, :, 0] = P_0

    
        


    for j in range(dim):
        
        Matrix = m(M=Mat, v=V[j], C=C[j])
            
        for k in range(len(x)-1):
            P[j, :, k+1] = P[j, :, k] * r(P[j, :, k], Matrix[k,:,:])
            # normalizing
            P[j, :, k+1] =  P[j, :, k+1]/(sum(np.absolute(P[j, :, k+1]))) 