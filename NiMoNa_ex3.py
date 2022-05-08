# I got pretty lazy and did not want to change the original code. My new way of implementing the changes is to 

import numpy as np
import matplotlib.pyplot as plt
# r returns the replicator
def r(x, M):
    return M.dot(x)/np.dot(x, M.dot(x))



def original_population_generator():
    # intitializing the parameters

    
    x = np.linspace(0, 15, 15)
    p = np.empty((4, 2, 15))
    fig, axs = plt.subplots(5, sharex=True)

    for V, C, p_0, p_1, d in [[1., 1.5, 0.5, 0.5, 0],[1.5, 1., 0.5, 0.5, 1],[1., 1.5, 0.1, 0.9, 2],[1., 1.5, 0.9, 0.1, 3]]:
        # Payoff matrix
        M = np.array([[(V-C)/2, V], [0,V/2]])
        
        # storing the population in a 3D-array
        p[d, 0:2, 0] = np.array([p_0, p_1])
        for i in range(p.shape[2]-1):
        
            p[d, :, i+1] = p[d, 0:2, i] * r(x = p[d, 0:2, i], M = M)
    
    # plotting the function and adjusting parameters
       # axs[d].plot(x, p[d, 0], label = "Hawks") 
      #  axs[d].plot(x, p[d, 1], label = "Doves")
     #   axs[d].set_title("V = {0}, C = {1}, P_0 = {2} = {3}".format(V, C, p_0, p_1))
    #axs[0].legend(loc="upper right")
    #axs[0].set_ylim([0,1])
    #axs[2].set_ylim([0,1])
    #plt.tight_layout()
    return p



def main():

    print(original_population_generator())
    
    











if __name__ == "__main__":
    main()