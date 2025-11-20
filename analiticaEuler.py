import numpy as np
import math
import matplotlib.pyplot as plt

#   Solución analítica
def solucion_analitica(t):
    return math.exp(t)

#   Ecuación diferencial: y' = y
def f(t, y):
    return y


#   Método de Euler
def euler(y0, t0, t_final, h):
    t_values = np.arange(t0, t_final + h, h)
    y_values = [y0]

    y = y0
    for i in range(1, len(t_values)):
        y = y + h * f(t_values[i-1], y)
        y_values.append(y)

    return t_values, y_values

# Parámetros
y0 = 1
t0 = 0
t_final = 1
h = 0.2

# Correr Euler
t_vals, y_euler = euler(y0, t0, t_final, h)

# Valores analíticos
y_exact = [solucion_analitica(t) for t in t_vals]

# Mostrar resultados
print("t\tEuler\t\tExacta")
for t, y_num, y_ex in zip(t_vals, y_euler, y_exact):
    print(f"{t:.1f}\t{y_num:.6f}\t{y_ex:.6f}")

# (Opcional) Graficar
plt.plot(t_vals, y_euler, 'o-', label="Euler")
plt.plot(t_vals, y_exact, 's--', label="Exacta")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.title("Comparación entre Euler y Solución Analítica")
plt.legend()
plt.grid(True)
plt.show()
