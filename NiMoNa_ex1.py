#I hope that everything works as intended, although I don´t think that this implementation is the most efficient.




import numpy as np
import matplotlib.pyplot as plt


def f1(a, h, a_0, lower_limit, upper_limit):
    #arrays containing all x- and analytically solved values of the function
    x = np.linspace(lower_limit, upper_limit, int((upper_limit-lower_limit)/h))
    analytical_sol = (lambda x: a_0 * np.exp(-a*x))(x)
    
    #numerically approximated values
    sol_y = [a_0]
    for i in range(len(x)-1):
        a_0 += -a *a_0 * h
        sol_y.append(a_0)

    return x, analytical_sol, np.array(sol_y)

def f2(w, x_0, v_0, h, lower_limit, upper_limit):
    # first need to get an approximation of v using euler in order to use this for a second approximation of x
    # x ~ - w**2 * x * h**2 * 1/2 + v * h
    
    x = np.linspace(lower_limit, upper_limit, int((upper_limit-lower_limit)/h))
    asol = (lambda t: np.sin(w*t))(x)

    vsol = [v_0]
    ysol = [x_0]
    for i in range(len(x)-1):
        v_0 += - w**2 * x_0 * h
        vsol.append(v_0)

        x_0 += - w**2 * x_0 * h**2 * 0.5 + v_0 * h
        ysol.append(x_0)
    return x, vsol, ysol, asol


    

    


def plot():   
    
    #first plot:

    lower_limit = 0
    upper_limit = 7

    fig, axs = plt.subplots(2, 2, sharex=True)

    for a, h, a_o, row, col in [[1, 0.5, 0.5, 0, 0],[1, 1, 0.5, 0, 1],[1, 0.01, 0.5, 1, 0],[3, 0.05, 3, 1, 1]]:
        b = f1(a, h, a_o, lower_limit, upper_limit)
        x = b[0]
        asol = b[1]
        soly = b[2]
   
        axs[row, col].plot(x, asol)
        axs[row, col].plot(x, soly)
        axs[row, col].set_title("a = {0}, h= {1}, a_0 = {2}".format(a, h, a_o))
    

    #setting up the second plot:
    
    fig, axs = plt.subplots(3, 3, sharex=True, sharey=True)
    
    w = 1
    x_0 = 0
    v_0 = 1
    lower_limit = 0
    upper_limit = 20 * np.pi
    for h, row in [[0.05, 0], [0.025, 1], [0.001, 2]]:
        axs[row][0].plot(f2(w, x_0, v_0, h, lower_limit, upper_limit)[0], f2(w, x_0, v_0, h, lower_limit, upper_limit)[1])
        axs[row][1].plot(f2(w, x_0, v_0, h, lower_limit, upper_limit)[0], f2(w, x_0, v_0, h, lower_limit, upper_limit)[2])
        axs[row][2].plot(f2(w, x_0, v_0, h, lower_limit, upper_limit)[0], f2(w, x_0, v_0, h, lower_limit, upper_limit)[3])
        axs[row][0].set_ylabel("h = {0}".format(h))
    axs[0][0].set_title("x'")     
    axs[0][1].set_title("x nach Euler")
    axs[0][2].set_title("sin(wx)")
    


    plt.show()


plot()

