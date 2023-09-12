prime_number = 0
number = int(input("Ingrese un entero positivo para saber si es primo o no: "))
for i in range(number-1, 1, -1):
    if number%i == 0:
        prime_number = 1
if prime_number==0:
    print(f"El numero {number} es primo.")
elif prime_number==1:
    print(f"El numero {number} no es primo.")
print(" ")