# EJERCICIO 1
paso = int(input("Ingrese la cifra del César que desee(pasos): "))
msj1 = input("Ingrese su primer mensaje: ")
msj2 = input("Ingrese su segundo mensaje: ")
msj3 = input("Ingrese su tercer mensaje: ")
msj4 = input("Ingrese su cuarto mensaje: ")
msj5 = input("Ingrese su quinto mensaje: ")

alf = "abcdefghijklmnñopqrstuvwxyz"
for letra in msj1:
    ind=alf.find(letra)
    if ind==(-1):
        print(end= letra)
    else:
        ind=(ind+paso)%27
        if ind==0: 
            print(end= "z")
        else:
            print(end=alf[ind])
print("")

for letra in msj2:
    ind=alf.find(letra)
    if ind==(-1):
        print(end= letra)
    else:
        ind=(ind+paso)%27
        if ind==0:
            print(end= "z")
        else:
            print(end=alf[ind])
print("")
    
for letra in msj3:
    ind=alf.find(letra)
    if ind==(-1):
        print(end= letra)
    else:
        ind=(ind+paso)%27
        if ind==0:
            print(end= "z")
        else:
            print(end=alf[ind])
print("")

for letra in msj4:
    ind=alf.find(letra)
    if ind==(-1):
        print(end= letra)
    else:
        ind=(ind+paso)%27
        if ind==0:
            print(end= "z")
        else:
            print(end=alf[ind])
print("")
    
for letra in msj5:
    ind=alf.find(letra)
    if ind==(-1):
        print(end= letra)
    else:
        ind=(ind+paso)%27
        if ind==0:
            print(end= "z")
        else:
            print(end=alf[ind])
print("")

# EJERCICIO 2
#2-Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el
#0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene.
#Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.
rep=1
digitos_pares=0
digitos_impares=0

while rep==1:
    num=int(input("Ingrese un numero entero positivo: "))
    
    if num<=0: 
        print("El numero ingresado no es valido, intente de nuevo")
        rep=1
    else:
        f_num=str(num)
        for i in range(len(f_num)):
            temp=int(f_num[i])
            if temp%2==0:
                digitos_pares=digitos_pares+1
            else:
                digitos_impares=digitos_impares+1
    print("¿Desea ingresa otro numero?")
    print("[1].Si")
    print("[0].No")
    rep=int(input())
print("La cantidad de digitos con valores pares fue de:",digitos_pares)
print("La cantidad de digitos con valores impares fue de:",digitos_impares)