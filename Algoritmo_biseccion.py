def Biseccion(F, a, b, tol, N = 100):

    if F(a) * F(b) >= 0: 
        return "Error: no hay cambio de signo en el intervalo"

    for k in range(1, N+1):
        c = ( a + b ) / 2.0
        if F(c) == 0 or ( b - a ) / 2.0 < tol:
            return c, k+1

        if F(a) * F(c) < 0:
            b = c
        else:
            a = c

    return "Se alcanzo el numero maximo de iteraciones sin converger."

#Ejemplo:
def f(x):
    return x**3 - x - 2

#Parametros iniciales
a = 1.0
b = 2.0
tolerancia = 1e-6

try:
    raiz, iteraciones = Biseccion(f, a, b, tol=tolerancia)
    print(f"¡Raíz encontrada con éxito!")
    print(f"Raíz aproximada: {raiz:.6f}")
    print(f"Número de iteraciones: {iteraciones}")
except Exception as e:
    print(f"Error: {e}")
