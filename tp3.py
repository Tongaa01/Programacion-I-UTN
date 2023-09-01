import math
#1-------------------------------------------------------------------------------
word = str(input("Ingrese una frase cualquiera  "))
for n in range(10):
  print(word)
print(" ")  
#2-------------------------------------------------------------------------------
age = int(input("Ingrese cual es su edad: "))
for n in range(age):
  if n == 0:
    print("En algun momento usted cumplio 1 año")
  else:
    print(f"En algun momento usted cumplio {n+1} años.")
print(" ")    
#3-------------------------------------------------------------------------------
counter = 0
final_word = ""
num = int(input("Ingrese un numero entero positivo: "))

if num < 0:
  print("Error: Usted ingreso un numero negativo")
else:
  for n in range(num + 1):
    if n % 2 == 0:
      counter = counter + 1

    else:
      temp = str(n)
      if temp == "1":
        final_word = final_word + temp
      else:
        final_word = final_word + "," + temp

print(final_word)
print(" ")
#4-------------------------------------------------------------------------------
final_word = ""
num = int(input("Ingrese un numero entero positivo: "))

if num < 0:
  print("Error: Usted ingreso un numero negativo.")
else:
  for n in range(num + 1):
    temp = str(n)
    if temp == "0":
      final_word = temp + final_word
    else:
      final_word = temp + "," + final_word

print(final_word)

print(" ")

#5-------------------------------------------------------------------------------(sofi)
i=int 
num=(int(input("Ingrese un numero: ")))

for i in range(num,0,-1):
  print(i, end= ",")
print(0)

print(" ")

#6-------------------------------------------------------------------------------(tonga)
triangle = int(input("Ingrese la altura del triángulo: "))
x=0
body="*"

while x <= triangle:
    print(body * x)
    x = x + 1

print(" ")

#7-------------------------------------------------------------------------------(E)
for n in range(11):
  print(f"Tabla del {n}")  
  for i in range(11):
    if n == 0 or i == 0:
      print("")
    else:
      print(f"{n}x{i}={n*i}")
print(" ")      
#8-------------------------------------------------------------------------------(tonga)
columns = int(input("Ingrese la cantidad de columnas: "))
columns=columns*2
for n in range(columns + 2):
  print("")
  for i in range(n - 1, 0, -2):
    if i % 2 == 0:
      numbers=1
    else:
      print(i, end=" ")

#9-------------------------------------------------------------------------------(E)
password="Excalibur"
check=0
while check==0:
  rep=str(input("Ingrese la contraseña: "))
  if rep==password:
    print("Bienvenido a Camelot")
    check=1
  else:
    print("Contraseña no valida, intenta de nuevo")
    check=0
print(" ")  

#10-------------------------------------------------------------------------------()#ME RINDO ESTE EJERCICIO ME ROMPIO



#11-------------------------------------------------------------------------------(E)
final_word = ""
word = str(input("Ingrese una palabra: "))
l = len(word)
for n in range(l-1 , -1, -1):
  final_word = final_word + word[n]
print(final_word)
print(" ")  

#12-------------------------------------------------------------------------------(sofiiiiiAAAwe)
phrase=str(input("Ingrese una frase: ")) 
letter=str(input("Ingrese una letra: ")) 

#Este lo hago


#13-------------------------------------------------------------------------------(Emilio)
print("Escriba cualquier cosa para escuchar eco, o")
print("escriba 'salir' para dejar de escuchar el eco:")
words = "example"
while words != "salir":
    words = input(">>> ")
    if words != "salir":
        echo = words
        print("Eco:", echo)
print("Saliste con éxito.")
#14-------------------------------------------------------------------------------()
num_1= int(input("Ingrese un número entero: "))
num_2 = int(input("Ingrese otro número entero: "))
print(" ")
if num_2 < num_1:
    switch = num_2
    num_2 = num_1
    num_1 = switch
print(f"Los números pares entre {num_1} y {num_2} son:")
for n in range(num_1, num_2+1, 1):
    if n%2 == 0:
        print(end=f"{n} ")
print(" ")
print(" ")
print(f"Los números impares entre {num_1} y {num_2} son:")
for n in range(num_1, num_2+1, 1):
    if n%2 != 0:
        print(end=f"{n} ")
print(" ")
print(" ")
#15-------------------------------------------------------------------------------()



#16-------------------------------------------------------------------------------()



#17-------------------------------------------------------------------------------()



#18-------------------------------------------------------------------------------()



#19-------------------------------------------------------------------------------()



#20-------------------------------------------------------------------------------(tonga)
read = 1
sumatory = 0
while read != 0:
    print("Ingrese números de a uno para sumarlos, o")
    read = int(input("ingrese 0 para dejar de agregar: "))
    sumatory = sumatory + read
    print("")
print(f"La sumatoria de los números ingresados es {sumatory}")
print(" ")
#21-------------------------------------------------------------------------------()
read = 1
biggest = 0
while read != 0:
    print("Ingrese un número o ingrese")
    read = int(input("0 para terminar: "))
    if read > biggest:
        biggest = read
print(f"El número más grande ingresado es el {biggest}")
print(" ")
#22-------------------------------------------------------------------------------()


#23-------------------------------------------------------------------------------()
bill = 0
bill_input = 1
while bill_input != 0:
    print("Ingrese el monto del producto,")
    bill_input = input("o 0 para terminar: ")
    bill = bill + bill_input
print(f"El monto total de la factura es de ${bill}")
print(" ")
#24-------------------------------------------------------------------------------()
bill = 0
bill_input = 1
while bill_input != 0:
    print("Ingrese el monto del producto,")
    bill_input = float(input("o 0 para terminar: "))
    if bill_input < 0:
        print("El monto ingresado es incorrecto, ingrese uno nuevo.")
    else:
        bill = bill + bill_input
if bill < 1000:
    print(f"El monto total de la factura es de ${bill}")
else:
    bill = bill * 0.9
    print(f"El monto total de la factura (con descuento incluido) es de ${bill}")
print(" ")
#25-------------------------------------------------------------------------------()
factorial_result = 1
factorial = int(input("Ingrese un entero para conocer su factorial: "))
if factorial == 0:
    print("El factorial de 0 es 1.")
elif factorial > 0:
    fact = factorial
    while factorial > 0:
        factorial_result = factorial_result * factorial
        factorial = factorial - 1
    print(f"El factorial de {fact} es {factorial_result}.")
else:
    print("No está definido el factorial de un número negativo.")