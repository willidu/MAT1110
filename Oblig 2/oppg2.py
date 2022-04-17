import numpy as np

def F(v):
    B = np.asarray([
        [1/6, -1/6, 0],
        [-1/6, 1/2, 2/3],
        [0, 1/6, -1/6]
    ])
    return np.einsum('ij, j -> i', B, v) + (1, 0, 1)

def fixpoint(F):
    i = 0
    x = (0, 0, 0)
    while np.sum(F(x)-x) > 10e-8:
        x = F(x)
        i += 1

    print(f'Fixpoint: {x}, n = {i}')
    return x, i

fixpoint(F)

"""
Fixpoint: [1.0000001  0.9999997  0.99999994], n = 40
"""
