import math


k = 9e9  


def calcular_fuerza(q_obj, x_obj, y_obj, q, x, y):
    dx = x - x_obj
    dy = y - y_obj
    
    r = math.sqrt(dx**2 + dy**2)
    
    if r == 0:
        return 0, 0
    
    
    F = k * (q_obj * q) / (r**2)
    
    
    Fx = F * (dx / r)
    Fy = F * (dy / r)
    
    return Fx, Fy



n = int(input("Ingrese el número de cargas: "))

cargas = []

for i in range(n):
    print(f"\nCarga {i+1}")
    q = float(input("Magnitud (C): "))
    x = float(input("Posición x: "))
    y = float(input("Posición y: "))
    cargas.append((q, x, y))



print("\n--- Carga objetivo ---")
q_obj = float(input("Magnitud (C): "))
x_obj = float(input("Posición x: "))
y_obj = float(input("Posición y: "))



Fx_total = 0
Fy_total = 0

for q, x, y in cargas:
    Fx, Fy = calcular_fuerza(q_obj, x_obj, y_obj, q, x, y)
    Fx_total += Fx
    Fy_total += Fy



F_total = math.sqrt(Fx_total**2 + Fy_total**2)



print("\n--- RESULTADOS ---")
print(f"Fuerza neta: <{Fx_total:.2e}, {Fy_total:.2e}> N")
print(f"Magnitud: {F_total:.2e} N")