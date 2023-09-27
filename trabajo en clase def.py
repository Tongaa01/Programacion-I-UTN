import funciones

num = int(input("Ingrese numeros, o 0 para salir: "))
while num!=0:
    print(f"La suma de los dígitos es de: {funciones.digit_counter(num)}")
    num = int(input(">>> "))