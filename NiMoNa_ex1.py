from turtle import up
import numpy as np
import matplotlib.pyplot as plt


def f1(a, h, a_0, lower_limit, upper_limit):
    
    x = np.linspace(lower_limit, upper_limit, int((upper_limit-lower_limit)/h))
    analytical_sol = (lambda x: a_0 * np.exp(-a*x))(x)
    
    sol_y = [a_0]
    for i in range(len(x)-1):
        a_0 += -a *a_0 * h
        sol_y.append(a_0)
    print(len(x), len(analytical_sol), len(sol_y))
    return x, analytical_sol, np.array(sol_y)

def f2(w, x_0, v_0, h, lower_limit, upper_limit):
    # first need to get a approximation of v using euler in order to use this for a second approximation for x
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
    print(len(x), len(vsol), len(ysol), len(asol))
    return x, vsol, ysol, asol


    

    


def plot():   
    
    lower_limit = 0
    upper_limit = 7

    fig, axs = plt.subplots(2, 2, sharex=True)

    for a, h, a_o, row, col in [[1, 0.5, 0.5, 0, 0],[1, 1, 0.5, 0, 1],[1, 0.01, 0.5, 1, 0],[3, 0.05, 3, 1, 1]]:
        b = f1(a, h, a_o, lower_limit, upper_limit)
        x = b[0]
        asol = b[1]
        soly = b[2]
        #print(x, asol, soly)
   
        axs[row, col].plot(x, asol)
        axs[row, col].plot(x, soly)
        print(a, h, a_o)
        axs[row, col].set_title("a = {0}, h= {1}, a_0 = {2}".format(a, h, a_o))
    


    
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
    axs[0][0].set_title("Ableitung")     
    axs[0][1].set_title("Euler-Methode")
    axs[0][2].set_title("sin(wx)")
    


    plt.show()


plot()

