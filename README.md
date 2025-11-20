# analitica_euler
una solución aplicando el método Euler para aproximar la solución 

en este proyecto se resuelve una ecuacion diferencial usando el metodo Euler, la cual previamente se ah echo una ecuacion analitica, como fin de comparar el resultado contra la solucion numerica obtenida usando el metodo Euler

la ecuacion usada: dy/dy = y, y(0) = 1

la solucion analitica es la siguiente:

empezamos con: dy/dt = y
despues separamos: 1/y dy = dt
integramos: in|y| = t + C
despejamos: y = Cet
usando la condicion inicial y(0) = 1:  C = 1

la solucion seria: y(t) = et

con el metodo Euler:

t ∈ [0,1]
usando: H = 0.2

la formula de Euler es: yn + h * f (tn, yn)
