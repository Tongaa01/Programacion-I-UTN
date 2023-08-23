print("Ingrese el día y la fecha con el siguiente formato: día, DD/MM.")
print("Ejemplo: martes, 12/5")
ingreso = input()
dia = ingreso[0:ingreso.find(",")].lower()
DD = int(ingreso[ingreso.find(",")+2:ingreso.find("/")])
MM = int(ingreso[ingreso.find("/")+1:])
#Ahora definimos la condición principal, que es que la fecha ingresada no sea correcta
if DD>31 or MM>12 or DD<1 or MM<1:
    print("Error: Fecha incorrecta (Ingrese un n° de fecha válido).")
#Una vez limpio de errores, pasamos a las condiciones de cada día
elif dia=="lunes": #En el dia lunes, martes y miércoles solo calculamos el porcentaje de aprobados.
    print("Hoy toca: Nivel inicial.")
    alumnos_aprobados = int(input("Ingrese la cantidad de alumnos aprobados: "))
    alumnos_desaprobados = int(input("Ingrese la cantidad de alumnos desaprobados: "))
    alumnos_aprobados_porcentaje = (alumnos_aprobados * 100) / (alumnos_aprobados + alumnos_desaprobados)
    print(f"El porcentaje de alumnos aprobados es del {alumnos_aprobados_porcentaje}%")
elif dia=="martes": #En el dia lunes, martes y miércoles solo calculamos el porcentaje de aprobados.
    print("Hoy toca: Nivel intermedio.")
    alumnos_aprobados = int(input("Ingrese la cantidad de alumnos aprobados: "))
    alumnos_desaprobados = int(input("Ingrese la cantidad de alumnos desaprobados: "))
    alumnos_aprobados_porcentaje = (alumnos_aprobados * 100) / (alumnos_aprobados + alumnos_desaprobados)
    print(f"El porcentaje de alumnos aprobados es del {alumnos_aprobados_porcentaje}%")
elif dia=="miercoles" or "miércoles": #En el dia lunes, martes y miércoles solo calculamos el porcentaje de aprobados.
    print("Hoy toca: Nivel avanzado.")
    alumnos_aprobados = int(input("Ingrese la cantidad de alumnos aprobados: "))
    alumnos_desaprobados = int(input("Ingrese la cantidad de alumnos desaprobados: "))
    alumnos_aprobados_porcentaje = (alumnos_aprobados * 100) / (alumnos_aprobados + alumnos_desaprobados)
    print(f"El porcentaje de alumnos aprobados es del {alumnos_aprobados_porcentaje}%")
elif dia=="jueves": #En el dia jueves, verificamos primero que el porcentaje sea un n° correcto, y luego imprimimos mensaje dependiendo del valor.
    print("Hoy toca: Práctica hablada.")
    porcentaje_asistencia = int(input("Ingrese el porcentaje de asistencia: "))
    if porcentaje_asistencia<1 or porcentaje_asistencia>100:
        print("Error, porcentaje mal ingresado.")
    elif porcentaje_asistencia>50:
        print("Asistió la mayoría.")
    else:
        print("No asistió la mayoría.")
elif dia=="viernes": #En el dia viernes, verificamos si es el inicio de un nuevo ciclo, y allí calculamos el arancel.
    print("Hoy toca: Inglés para viajeros.")
    if (DD==1 and MM==1) or (DD==1 and MM==7):
        print("Comienzo de nuevo ciclo.")
        cant_alumnos = int(input("Ingrese la cantidad de alumnos en este ciclo: "))
        arancel = int(input("Ingrese el monto a pagar por cada alumno: "))
        total_dinero = cant_alumnos * arancel
        print(f"Por {cant_alumnos} alumnos, deberán pagar cada uno ${arancel}, sumando un total de ${total_dinero}")
elif (dia!="lunes" or dia!="martes" or dia!="miercoles" or dia!="miércoles" or dia!="jueves" or dia!="viernes"):
    print("Error: Fecha incorrecta (Ingrese un día correcto de la semana).")