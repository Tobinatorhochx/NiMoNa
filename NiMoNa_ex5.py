
#documentation: nmn.gen_C(c = const., rw=True/False, ocs=[[Amplitude],[Frequency],[Phase shift]] , x=array, dim=int)
import numpy as np
from matplotlib import pyplot as plt
import NiMoNa as nmn

def main(steps=200, dim=4):



    # initializing needed Parameters
    x = np.linspace(0, steps, steps)
    P_0 = np.array([[0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5]])
    V = nmn.gen_V(c=1.5, rw=True, osc=[[1, 2, 3, 4], [np.pi/2, np.pi/2, np.pi/2, np.pi/2], [0, 0, 0, 0]], x=x, dim=dim)
    C = nmn.gen_C(c=1.5, rw=True, x=x, dim=dim) 
    P = nmn.pop_development(C=C, x=x, P_0=np.array([0.5, 0.5]), V=V, steps=steps, dim=dim)
    
    fig, axs = plt.subplots(dim, sharex=True)

    for i in range(dim):
        
        axs[i].plot(x, P[i, 0, :])
        axs[i].plot(x, P[i, 1, :])
    plt.show()


if __name__ == "__main__":
    
    main()
    