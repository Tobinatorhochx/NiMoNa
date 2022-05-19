import matplotlib.pyplot as plt
import numpy as np

"""
def r(p, M):
    return M.dot(p)/np.dot(p, M.dot(p))
f = np.pi/2
C = 1.5
A = 1
V = lambda A, x, f: 1 + A * np.sin(f * x)

x = np.linspace(0, 15, 16)
M = np.empty(64, dtype=float).reshape((16, 2, 2))# into z, x, y direktion
P = np.empty((2, 16))
P[:, 0] = np.array([0.5, 0.5])
V = V(A, x, f)








for i in range(len(x)):
    M[i, 0, 0] = np.float64((V[i]-C)/2)
    M[i, 0, 1] = np.float64(V[i])
    M[i, 1, 0] = 0
    M[i, 1, 1] = np.float64(V[i]/2)

print(M)
for i in range(len(x)-1):
    P[:, i+1] = P[:, i] * r(P[:, i], M[i])

plt.plot(x, P[0], x, P[1])
plt.show()
"""

A = [0.1, 1, 10]
C = 1.5
x = np.linspace(0, 100, 101)

f = [1, np.pi/2, np.pi/2]
V_x = np.array([(lambda A, x, f: 1 + A * np.sin(f*x))(A, x, f) for A, f in zip(A, f)])
print(V_x)

print(len([]))