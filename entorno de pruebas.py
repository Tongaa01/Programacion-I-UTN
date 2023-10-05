import funciones, math, sys
sys.set_int_max_str_digits(0)
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
        print(prime_list)
digit = int(input("Ingrese un número para buscar cuántas veces aparece: "))
print(f"El número {digit} aparece {funciones.frequency_digit_counter(prime_list,digit)} veces.")
print(f"El factorial del primo más grande ingresado ({biggest_number}) es {math.factorial(biggest_number)}.")