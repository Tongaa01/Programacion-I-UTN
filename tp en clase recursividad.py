# 1 ------------------------------------------------------------------------------------------
import random

def rat_path(taken_time):
    paths = random.randint(1,3)
    if paths==1:
        taken_time = taken_time + 3
        print(f"La rata eligió el camino {paths}, volvió a la jaula.")
        print(f"Tiempo sin salir: {taken_time}")
        rat_path(taken_time)
    elif paths==2:
        taken_time = taken_time + 5
        print(f"La rata eligió el camino {paths}, volvió a la jaula.")
        print(f"Tiempo sin salir: {taken_time}")
        rat_path(taken_time)
    elif paths==3:
        taken_time = taken_time + 7
        print(f"La rata eligió el camino {paths}, y logró salir de la jula.")
        print(f"Tiempo total en escapar: {taken_time}")
taken_time = 0
rat_path(taken_time)

# 2 ------------------------------------------------------------------------------------------
# Tengo un espejo, que invierte los dígitos de un número. Escriba un programa que haga lo que hace el espejo.