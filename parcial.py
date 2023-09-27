user = str(input("Ingrese su nombre: ")).title()
print(f"Bienvenido, {user}! Elija uno de los siguientes juegos:")
print("[1]. Juego de números.")
print("[2]. Juego de palabras.")
while True:     #Acá verificamos que solo ingrese una de las opciones dadas y no ninguna otra cosa
    choice = input(">>> ")
    if choice=="1" or choice=="2":
        choice = int(choice)
        break
    else:
        print("Error, ingrese una de las opciones dadas (1 o 2).")
        continue
if choice==1:
    print(f"Okay {user}! Ha elegido el juego n°{choice}. Las reglas son las siguientes:")
    print("1. Ingrese números enteros.")
    print("2. Para salir, ingrese 0.")
    numbers = 1
    numbers_even = 0
    numbers_odd_counter = 0
    numbers_odd_final = 0
    while numbers!=0:
        numbers = input(">>> ")
        numbers_checker = numbers.isdigit()     #Acá verificamos que solo ingrese números enteros
        if numbers_checker==True:
            numbers = int(numbers)
            if numbers%2==0 and numbers>numbers_even:
                numbers_even = numbers
            elif numbers%2!=0:
                numbers_odd_counter = numbers_odd_counter + 1
                numbers_odd_final = numbers_odd_final + numbers
            continue
        else:
            print("Error, ingrese solo números enteros")
            continue
    print(f"{user}, salió con éxito")
    print(f"El número par más alto ingresado es el {numbers_even}")
    print(f"El promedio entre los {numbers_odd_counter} n° impares que ingresó es {numbers_odd_final/numbers_odd_counter}")
elif choice==2:
    print(f"Okay {user}! Ha elegido el juego n°{choice}.")
    print("Por favor, ingrese una frase para saber cuántas de cada vocal tiene la misma:")
    phrase = input(">>> ")
    a_counter = phrase.count("a")       #Acá contamos cada una de las vocales
    e_counter = phrase.count("e")
    i_counter = phrase.count("i")
    o_counter = phrase.count("o")
    u_counter = phrase.count("u")
    print(f"{user}, la frase ingresada tiene las siguientes vocales:")
    print(f"[a]={a_counter}; [e]={e_counter}; [i]={i_counter}; [o]={o_counter}; [u]={u_counter}")