import math
#1 english----------------------------------------------------------()
x = 0
while x <= 30:
  x = x + 1
  if x==4 or x==6 or x==10:
    print(f"Se saltó el el valor {x} de x.")
  elif x==15:
    print(f"Se rompió la ejecución del bucle cuando x valía {x}.")
    break
  else:
    print(x)
print("")
#1------------------------------------------------------------------(E)
list = []
exit = True
line_number = int(input("Cuantas lineas desea ingresar  "))
for i in range(line_number):
  temp = str(input("Ingrese una linea  "))
  list = list + [temp]
print("")  
while exit == True:
  for p in range(line_number):
    print(list[p].upper())
  break  
print("")
#2------------------------------------------------------------------(Tonga)
bank_account = 0
bank_movements = 0
print("Bienvenido a Dinamite Bank. Las operaciones disponibles son:")
print("Retiros: R y el monto, ejemplo: R 200")
print("Depósitos: D y el monto, ejemplo: D 500")
print("Salir: Deje el espacio vacío y presione 'enter'")
while True:
    bank_input = input("Ingrese la operación y el monto con el formato dado:").upper()
    bank_operation = bank_input[0]
    if len(bank_input)>1:
        bank_movements = float(bank_input[2:])
    if bank_operation=="D":
        if bank_movements<0:
            print("Error. No puede depositar negativamente. Intente nuevamente.")
        else: 
            bank_account = bank_account + bank_movements
    elif bank_operation=="R":
        if bank_movements<0:
            print("Error. No puede retirar negativamente. Intente nuevamente.")
        elif (bank_account-bank_movements)<0:
            print(f"Error. No puede retirar más fondos de los que ya tiene (${bank_account}). Intente nuevamente.")
        else:
            bank_account = bank_account - bank_movements
    elif bank_operation=="":
        break
    else:
        print("Error. Ingrese una operación con el formato dado")
print(f"Ha salido con éxito. Su balance es de ${bank_account}")
print("")
#3------------------------------------------------------------------()
#Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, 
#finalizando cuando se reciba un cero.
#Imprimir la cantidad total de números primos ingresados.
#Nota: Un número primo es un número natural mayor que 1 que tiene únicamente dos divisores distintos:
#él mismo y el 1.
#let me in, letme innnnnnn
n=0
primo=0
NoPrimo=0
while True:
    num = int(input("Ingrese números:")) 
    if num<0:
        print("Error, ingrese un numero mayor a uno:")
        continue
    elif num == 0 :
        break
        #si es divisible NO es PRIMO
    else:
        for i in range(2, num, 1):
            if num%i == 0:
                NoPrimo = num
            else:
               primo = primo + 1
print("La cantidad de números PRIMOS ingresados es: ",primo)
print("")
#4------------------------------------------------------------------()




#5------------------------------------------------------------------()
print("Los numeros pares entre el 1 y el 20 son:")
for i in range(1, 21, 1):
  if i % 2 != 0:
    continue
  else:
    print(i)
print("")
#6------------------------------------------------------------------()
list = [1, 18, 3, 4, 10, 6, 12, 8, 20, 5, 11, 7, 13, 14, 15, 16, 17, 2, 19, 9]
exit = 1
while exit == 1:
  num_look = int(input("¿Que numero entre el 1 y 20 desea buscar? "))
  if num_look < 1 or num_look > 20:
    print("Ese numero no esta comprendido entre 1 y 20")
    print("Intente denuevo")
    exit = 1
  else:
    exit = 0

for i in range(1, 21, 1):
  if list[i] == num_look:
    print(f"Numero {num_look} encontrado en la posición {i+1}")
    break
print("")
#7------------------------------------------------------------------()
import random

exit = True
while exit == True:
  print("")
  print("¡Elige una opcion si te atreves!")
  print("[1].Sorpresa")
  print("[2].50% ganas un millon de dolares 50%¡Mueres!")
  print("[3].Puedes ver que hay dentro de la caja misteriosa")
  print("[0].Salir :(")
  rep = int(input())
  print("")
  if rep == 1:
    print("¡Feliz cumpleaños!")
  elif rep == 2:
    num = random.randint(1, 2)
    if num == 1:
      print("Señoras y señores me complace anunciar que usted gano.... ¡UN MILLON DE DOLARES!")
    elif num == 2:
      print("Me temo que moriste...¡PERO SOBREVIVISTE!")
  elif rep == 3:
    num2 = random.randint(1, 6)
    if num2 == 1:
      print("Dentro de la caja hay...¡un vaso de leche!")
    elif num2 == 2:
      print("Dentro de la caja hay...¿Una piton?")
    elif num2 == 3:
      print("Dentro de la caja hay...¡Un chocolate milka!")
    elif num2 == 4:
      print("Dentro de la caja hay...¡Un cupon para un viaje!")
    elif num2 == 5:
      print("Dentro de la caja hay...¿Nada?")
    elif num2==6:
     print("Dentro de la caja hay...¡Un dinosaurio de plastico!")
  elif rep == 0:
    print("¡No me dejes!")
    break