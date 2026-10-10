import numpy as np
import matplotlib.pyplot as plt

def thomas(a, b, c, d):

    n = len(d)

    a = a.copy(); b = b.copy(); c = c.copy(); d = d.copy();

    # Eliminacion hacia adelante
    for i in range(1, n):
        m = a[i] / b[i - 1]

        b[i] = b[i] - m * c[i - 1]
        d[i] = d[i] - m * d[i - 1]

    # Sustitucion hacia atras
    x = np.zeros(n)

    x[n - 1] = d[n - 1] / b[n - 1]

    for i in range(n - 2, -1, -1):
        x[i] = (d[i] - c[i] * x[i + 1]) / b[i]

    return x

n = 10
h = 1 / n

x = np.linspace(0, 1, n + 1)

N = n - 1
# Diagonal inferior
a = np.ones(N)
# Diagonal principal
b = -2 * np.ones(N)
# Diagonal superior
c = np.ones(N)
# Vector del lado derecho
d = -2 * h**2 * np.ones(N)

# Resolver con Thomas

u_interior = thomas(a, b, c, d)

u = np.zeros(n + 1)

u[1:n] = u_interior

u_exacta = -x**2 + x

print("   x          Aproximacion        Exacta")

for i in range(n + 1):
    print(f"{x[i]:.2f}       {u[i]:.8f}       {u_exacta[i]:.8f}")

# Error maximo
error = np.max(np.abs(u - u_exacta))
print("\nError maximo =", error)

# Grafica
plt.plot(x, u, 'o-', label='Numerica')
plt.plot(x, x - x**2, label='Exacta')
plt.legend()
plt.grid()
plt.show()