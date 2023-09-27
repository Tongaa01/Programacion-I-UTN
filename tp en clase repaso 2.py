# EJERCICIO 1
while True:
    char = input("Ingrese una frase o palabra: ")
    if len(char)==0:
        print("No puede dejar este espacio en blanco")
        continue
    elif len(char)<=4:
        char = char + "!"
        break
    else:
        char = char + "?"
        break
print(char)
print(" ")
# EJERCICIO 2


# EJERCICIO 3
counter = 1
char = input("Ingrese una frase: ")
if len(char)==0:
    print("No puede dejar este espacio vacío")
for i in range(0, len(char), 1):
    if char[i]==" ":
        counter = counter + 1
print(f"La frase contiene {counter} palabras")
print(" ")
# EJERCICIO 4


# EJERCICIO 5


# EJERCICIO 6


# EJERCICIO 7