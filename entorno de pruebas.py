prime = 0
prime_number = 0
while True:
    num = int(input("Ingrese números mayores a 0 (o 0 para salir): "))
    if num==0:
       break
    elif num<0:
       print("Solo puede ingresar números positivos.")
       continue
    for i in range(num-1, 1, -1):
       if num%i==0:
           prime_number = 1
    if prime_number == 0:
       prime = prime + 1
       continue
    elif prime_number==1:
       prime_number = 0
       continue
    
print(f"usted ha ingresado {prime} números primos.")
    



    
