import numpy as np

def gradiente_conjugado(A, b, x0, tol=1e-5, max_iter=1000):
    x = np.array(x0, dtype=float)
    r = b - np.dot(A, x)
    p = np.copy(r)
    k = 0
    
    while np.linalg.norm(r) > tol and k < max_iter:

        Ap = np.dot(A, p)
        alpha = np.dot(r, r) / np.dot(p, Ap)
        x = x + alpha * p
        r_anterior = np.copy(r)
        r = r - alpha * Ap
        beta = np.dot(r, r) / np.dot(r_anterior, r_anterior)
        p = r + beta * p

        k += 1

    return x

# Ejemplo de uso:
if __name__ == "__main__":
    # Definimos una matriz simétrica y definida positiva A
    A = np.array([[4.0, 1.0], 
                  [1.0, 3.0]])
    
    b = np.array([1.0, 2.0])
    x0 = np.array([0.0, 0.0])
    tol = 1e-6

    x_solucion = gradiente_conjugado(A, b, x0, tol)
    
    print("------Metodo del Gradiente conjugado------")
    print("Solución encontrada:", x_solucion)
    print("Verificación A * x:", np.dot(A, x_solucion))