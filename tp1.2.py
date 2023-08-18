# TRABAJO PRÁCTICO 1.2

# EJERCICIO 1
base = float(input("Ingrese la base del triángulo:"))
altura = float(input("Ingrese la altura:"))
area = (base * altura) / 2
lado1 = float(input("Ingrese el valor del primer lado:"))
lado2 = float(input("Ingrese el valor del segundo lado:"))
lado3 = float(input("Ingrese el valor del tercer lado:"))
perimetro=print("El perímetro del triangulo es: ",(lado1+lado2+lado3))
print("El área del triangulo es: ",area)
print(" ")

# EJERCICIO 2
print("Dé las longitudes de los catetos")
cat1 = float(input("Cateto 1:"))
cat2 = float(input("Cateto 2:"))
hipot = (cat1**2 + cat2**2)**(1/2)
print("La hipotenusa de dicho triángulo mide", hipot)
print(" ")

# EJERCICIO 3
num1= float(input("Ingrese un número: "))
num2= float(input("Ingrese otro número: "))
sum= num1+num2
rest= num1-num2
multp= num1*num2
div= num1/num2
print("Segun los números ingresados:")
print("suma:",sum, "\nresta:",rest, "\nmultiplicación:",multp,"\ndivision:",div)
print(" ")

# EJERCICIO 4
grados_f=float(input("Ingrese grados Fahrenheit: "))
grados_c=((grados_f-32)*5/9)
print(grados_f," equivalen a ",grados_c," grados celcius.")
print(" ")

# EJERCICIO 5
#¿Qué problemas tienen las siguientes instrucciones?¿Cómo las solucionarías?

#a) A = input(nombre, “¿Cuál es tu canción favorita?”)
# No se puede poner una variable dentro de un input.
A = (input("¿Cual es tu canción favorita? "))

#b)	precio = input(“Precio: “)
#   total = precio + (precio * 0.1)
# Falta poner que tipo de variable esta pidiendo, en la entrada de datos de precio.
precio = float(input("Precio: "))
total = precio + (precio*0.1)

#c)	edad = int(input(“Edad: “))
#   print(tu edad es, edad)
#  el texto no está entre comillas, por lo que no cuenta


#d)	edad = int(input(“Edad: “))
# print(“Veamos si tu edad es 18…”, edad=18)

# EJERCICIO 6
print("Ingrese el primer numero: ")
num1=float(input())
print("Ingrese el segundo numero: ")
num2=float(input())
print("Ingrese el tercer numero: ")
num3=float(input())
promedio=(num1+num2+num3)/3
print("El promedio de los numeros dados es:", promedio)
print(" ")

# EJERCICIO 7
print("Ingrese la cantidad de minutos que desee: ")
minutos=int(input())
horas=int(minutos/60)
print(minutos," equivalen a ",horas," horas y ",minutos-(horas*60)," minutos.")
print(" ")

# EJERCICIO 8
sueldo_base = float(input("Ingrese su sueldo base: "))
comision = 0.10
venta1 = float(input("Ingrese el monto de la primer venta: "))
venta2 = float(input("Ingrese el monto de la segunda venta: "))
venta3 = float(input("Ingrese el monto de la tercera venta: "))
sueldo_final = str(sueldo_base + comision*venta1 + comision*venta2 + comision*venta3)
print(f'Su sueldo final será de {sueldo_final}')
print(" ")

# EJERCICIO 9
precio_total = float(input("Ingrese el precio neto: "))
print("El precio con descuento del 15 por ciento es de: $", precio_total*0.85)
print(" ")

# EJERCICIO 10
parcial1 = float(input("Ingrese la nota del parcial 1: "))
parcial2 = float(input("Ingrese la nota del parcial 2: "))
parcial3 = float(input("Ingrese la nota del parcial 3: "))
prom_parciales = ((parcial1 + parcial2 + parcial3 ) / 3) * 0.55
final = float(input("Ingrese la nota del Final:"))
final = final * 0.30
trabajo_final = float(input("Ingrese la nota del TP Final: "))
trabajo_final = trabajo_final * 0.15
nota_final = prom_parciales + final + trabajo_final
print("La nota final de la materia es de:", nota_final)
print(" ")

# EJERCICIO 11
x1 = float(input("Ingrese un número: "))
x2 = float(input("Ingrese otro número: "))
distancia = abs(x1 - x2)
print("La distancia entre dichos números es de:", distancia)
print(" ")

# EJERCICIO 12
numero = float(input("Ingrese un número: "))
print("La raiz cuadrada del n° es:", numero**(1/2), " y la raiz cúbica es:", numero**(1/3))
print(" ")

# EJERCICIO 13


# EJERCICIO 14


# EJERCICIO 15


# EJERCICIO 16


# EJERCICIO 17
usuario = input("Ingrese su nombre: ")
print(f"Ahora estas en la matrix, {usuario}")

# EJERCICIO 18
comanda = float(input("Ingrese el valor de la comida: "))
servicio = comanda * 0.062
propina = comanda * 0.1
print(end= "Valor de la comida: $")
print(comanda)
print(end= "Costo del servicio: $")
print(servicio)
print(end= "Propina: $")
print(propina)
print(end= "Precio final: $")
print(comanda + servicio + propina)
print(" ")

# EJERCICIO 19


# EJERCICIO 20


# EJERCICIO 21
consumo = float(input("Ingrese la cantidad recorrida promedio con 1l de combustible: "))
tanque = float(input("Ingrese la capacidad del tanque: "))
recorrido = float(input("Ingrese cuántos kilómetros va a recorrer: "))
num_final = (recorrido / consumo) / tanque
print(f"En total va a necesitar {num_final} tanques de combustible para realizar el viaje")