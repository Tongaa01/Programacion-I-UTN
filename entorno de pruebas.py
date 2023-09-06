bill = 0
bill_input = 1
while bill_input != 0:
    print("Ingrese el monto del producto,")
    bill_input = float(input("o 0 para terminar: "))
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