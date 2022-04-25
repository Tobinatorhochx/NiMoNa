import numpy as np
import matplotlib.pyplot as plt


def r(x, M):
    return M.dot(x)/np.dot(x, M.dot(x))

def main():

#intitializing the parameters


    x = np.linspace(0, 15, 15)
    p = np.resize(x, (4, 2, 15))
    fig, axs = plt.subplots(4, sharex=True)

    for V, C, p_0, p_1, d in [[1, 1.5, 0.5, 0.5, 0],[1.5, 1, 0.5, 0.5, 1],[1, 1.5, 0.1, 0.9, 2],[1, 1.5, 0.9, 0.1, 3]]:
        M = np.array([[(V-C)/2, V], [0,V/2]])

        p[d, 0:2, 0] = np.array([p_0, p_1])
        for i in range(p.shape[2]-1):
            p[d, 0:2, i+1] = p[d, 0:2, i] * r(x = p[d, 0:2, i], M = M)
            #axs[d].plot(x, p[d, 0], x, p[d, 1])
    print(p)

    axs[0].plot(x, p[0, 0], x, p[0, 1])
    axs[0].set_ylabel("V = 1, C = 1.5, P_0 = P_1 =  0.5")
    axs[1].plot(x, p[1, 0], x, p[1, 1])
    axs[1].set_ylabel("V = 1.5, C = 1, P_0 = P_1 =  0.5")
    axs[2].plot(x, p[2, 0], x, p[2, 1])
    axs[2].set_ylabel("V = 1.5, C = 1, P_0 = 0.1, P_1 =  0.9")
    axs[3].plot(x, p[3, 0], x, p[3, 1])
    axs[3].set_ylabel("V = 1.5, C = 1, P_0 = 0.9, P_1 =  0.1")
        #plt.plot(x, p[0], label = "Hawk")
        #plt.plot(x, p[1], label = "Dove")
    #plt.axis(ymin=0, ymax=1)
    #plt.legend()

    plt.show()
main()
#
#
