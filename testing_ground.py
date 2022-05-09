import numpy as np

C = [1.5 for x in range(5)]
V = [lambda t: 1 + A * 0.1 * np.sin(t) for A in range(1, 1001, 200)]

x = np.linspace(0, 5, 6)
print(np.arange(14).reshape(2, 7)[:, 4], sum(np.arange(14).reshape(2, 7)[:, 4]))
V = [(lambda t, k: 1 + 0.1 * k*  np.sin(t)) for y in range(2)]
for f, k in zip(V, [x for x in range(len(V))]):
    print(f(3, k))

