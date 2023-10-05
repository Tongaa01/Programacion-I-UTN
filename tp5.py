import math, funciones
# 1 ------------------------------------------------------------------

# 2 ------------------------------------------------------------------
phrase = input("Ingrese una frase a continuación: ")
flipped_phrase_list = phrase[len(phrase)::-1]
print(f"La longitud de la última palabra es: {funciones.last_word_len(flipped_phrase_list)}")
print("")
# 3 ------------------------------------------------------------------

# 4 ------------------------------------------------------------------

# 5 ------------------------------------------------------------------
day_num = int(input("Ingrese la cantidad de días a visualizar: "))
num = 1
while num<=day_num:
    min_temp = float(input("Ingrese la temperatura mínima: "))
    max_temp = float(input("Ingrese la temperatura máxima: "))
    print(f"La temperatura promedio del dia {num} es de:", funciones.prom_temp(min_temp,max_temp))
    num = num + 1
print("")
# 6 ------------------------------------------------------------------

# 7 ------------------------------------------------------------------

# 8 ------------------------------------------------------------------

# 9 ------------------------------------------------------------------

# 10 ------------------------------------------------------------------

# 11 ------------------------------------------------------------------

# 12 ------------------------------------------------------------------

# 13 ------------------------------------------------------------------

# 14 ------------------------------------------------------------------
prime_number = int(input("Ingrese un número para ver si es primo o no: "))
prime = funciones.prime_checker(prime_number)
if prime==True:
    print(f"El número {prime_number} es primo.")
elif prime==False:
    print(f"El número {prime_number} no es primo.")
print("")
# 15 ------------------------------------------------------------------

# 16 ------------------------------------------------------------------

# 17 ------------------------------------------------------------------
print("Ingrese números primos, o uno no primo para salir:")
prime_list = []
prime_number = True
biggest_number = 0
while True:
    num = int(input(">>> "))
    prime_number = funciones.prime_checker(num)
    if prime_number==False:
        break
    else:
        if num>biggest_number:
            biggest_number = num
        temp = list(map(int, str(num)))
        prime_list.extend(temp)
        print(f"Suma de los dígitos de {num}: {funciones.digit_counter(num)}.")
digit = int(input("Ingrese un número para buscar cuántas veces aparece: "))
print(f"El número {digit} aparece {funciones.frequency_digit_counter(prime_list,digit)} veces.")
print(f"El factorial del primo más grande ingresado ({biggest_number}) es {math.factorial(biggest_number)}.")