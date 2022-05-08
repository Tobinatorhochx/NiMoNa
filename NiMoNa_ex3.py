# A relatively unfinished version. As of right now, all populations are reaching pretty much the same stable state. I tried 
# to make easy changes to that by bumping up the multiplicator for the doves and lowering the multiplicator for the hawks, but all I reached was
# that the population reaches a level that isn´t normed to 1 anymore. The population of the doves is still at zero, which is unfortunate for #
# them.

import numpy as np
import matplotlib.pyplot as plt


# r returns the replicator
def r(x, M):
    #print(x)
    return M.dot(x)/np.dot(x, M.dot(x))
# nextneighbor returns the updated values of the population after influences by neighboring populations have been taken into account
def nextneighbor(p, d, i, res):
    # the interaction network between the populations. I added an intermediate holder for the variables because I did not want to change 
    # variables while still in the process.
    for k in range(d):
        if k == 0:
            res[k, 0] = p[k, 0, i] * 1.1
            res[k, 1] = p[k, 1, i] * 1.8 * 0.9 * p[1,1, i] + 0.2
            
        if k == 1:
            res[k, 0] = p[k, 0, i] + 1.7 * p[2, 1, i]
            res[k, 1] = p[k, 1, i] * 1.8 * p[0, 1, i] + 0.3
        if k == 2:
            res[k, 0] = 0.4 * (1.4 *p[k, 0, i] * 0.7 * p[1, 0, i]) -0.1
            res[k, 1] = 0.9 * 1.4 * p[k, 1, i]
        if k == 3:
            res[k, 0] = 0.8 * p[k, 0, i]
            res[k, 1] = 3.2 * p[k, 1, i]
    return res



def main():
    fig, axs = plt.subplots(4, sharex=True)
    
    x = np.linspace(0, 15, 15)
    p = np.empty((4, 2, 15))
    intermediate_results = np.empty((4, 2))
    
    # initiating the starting population
    for p_0, p_1, d in [[0.5, 0.5, 0], [0.5, 0.5, 1], [0.1, 0.9, 2], [0.9, 0.1, 3]]:
        p[d, 0:2, 0] = np.array([p_0, p_1])
        

    # simultaneously calculating the replicator of the system alone while other 
    for i in range(p.shape[2]-1):
        for V, C, d in [[1., 1.5, 0],[1.5, 1., 1],[1., 1.5, 2],[1., 1.5, 3]]:
            M = np.array([[(V-C)/2, V], [0,V/2]])

            p[d, :, i+1] = p[d, 0:2, i] * r(x = p[d, 0:2, i], M = M)
            
        p[:,:,i+1] = nextneighbor(p, p.shape[0], i+1, intermediate_results)
    
    #plotting the function and adjusting parameters
    for j in range(p.shape[0]):
        
        axs[j].plot(x, p[d, 0], label = "Hawks") 
        axs[j].plot(x, p[d, 1], label = "Doves")
    #Boilerplate for the layout, might correct that later.
        #axs[d].set_title("V = {0}, C = {1}, P_0 = {2} = {3}".format(V, C, p_0, p_1))
        #axs[0].legend(loc="upper right")
        #axs[0].set_ylim([0,1])
        #axs[2].set_ylim([0,1])
        #plt.tight_layout()
    
    plt.show()
    
    




if __name__ == "__main__":
    main()