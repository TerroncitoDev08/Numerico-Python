import numpy as np

def householder_qr(A):
    m,n = A.shape
    Q = np.eye(m)
    R = np.copy(A)

    for j in range(min(m - 1, n)):
        x = R[j: , j]
        norm_x = np.linalg.norm(x)

        if norm_x == 0:
            continue
    #Calcular el vector de Householder
    alpha = -np.copysign(norm_x, x[0])
    v[0] -= alpha
    norm_v = np.linalg.norm(v)

    if norm_v != 0:
        v /= norm_v

    #Construir la matriz de Householder H_j
    H_sub = np.eye(m - j) - 2.0 * np.outer(v , v)
    H = np.eye(m)
    H[j: , j:] = H_sub

    #Actualizar R y Q
    R = np.dot(H, R)
    Q = np.dot(Q , H)

    return Q , R
    