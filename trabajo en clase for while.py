# EJERCICIO 1
paso = int(input("Ingrese la cifra del César que desee(pasos): "))
msj1 = input("Ingrese su primer mensaje: ")
msj2 = input("Ingrese su segundo mensaje: ")
msj3 = input("Ingrese su tercer mensaje: ")
msj4 = input("Ingrese su cuarto mensaje: ")
msj5 = input("Ingrese su quinto mensaje: ")

alf = "abcdefghijklmnopqrstuvwxyz"

for letra in msj1:
    ind=alf.find(letra)
    ind=(ind+paso)%27
    print(end=alf[ind])
print("")

for letra in msj2:
    ind=alf.find(letra)
    ind=(ind+paso)%27
    print(end=alf[ind])
print("")
    
for letra in msj3:
    ind=alf.find(letra)
    ind=(ind+paso)%27
    print(end=alf[ind])
print("")

for letra in msj4:
    ind=alf.find(letra)
    ind=(ind+paso)%27
    print(end=alf[ind])
print("")
    
for letra in msj5:
    ind=alf.find(letra)
    ind=(ind+paso)%27
    print(end=alf[ind])
print("")
    