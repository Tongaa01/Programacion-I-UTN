# Aquí definimos las variables, siendo "numero1" entera y "numero2" decimal.
numero1 = 8 
numero2 = 2.5

# Ahora definimos las distintas operaciones: suma, resta, multiplicación y división.
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

# Imprimimos los resultados de cada operación.
print(numero1, "+", numero2, "=", suma)
print(numero1, "-", numero2, "=", resta)
print(numero1, "*", numero2, "=", multiplicacion)
print(numero1, "/", numero2, "=", division)

# Ahora declaramos variables nuevas e imprimimos los precios.
nombre = "Gastón Astudillo"
precio = 1750
descuento = 0.25
precio_final = precio - (precio * descuento)

print("Precio original: $", precio)
print("Precio con descuento aplicado: $", precio_final)

# Agregamos una variable de cadena y trabajamos con ella.
cadena = "Nadie puede detener a un hombre con un propósito."
longitud = len(cadena)
print(cadena)
print("Longitud de la cadena:", longitud, "caracteres.")

# Volvemos a trabajar con al variable "precio".
precio = 12.3
print("Precio completo: $", precio)
print("Precio redondeado: $", int(precio))

# Trabajamos para concatenar 2 variables.
nombre = "Gaston"
apellido = "Astudillo"
nombre_completo = nombre + " " + apellido
print(nombre_completo)

# Ahora trabajamos con una variable con mi edad y con mi estatura.
edad = 22
print("Mi edad actual:", edad)
print("Mi edad dentro de 5 años:", edad + 5)
print("Mi edad hace 10 años:", edad - 10)
altura = 1.85
print("Mi estatura:", altura, "m")
print("Mi estatura si fuera 4 veces mas grande:", altura * 4, "m")
print("Mi estatura si fuera 3 veces mas chico:", altura / 3, "m")

# Jugamos con las mayúsculas y minúsculas
nombre_completo = "GASTON ASTUDILLO"
print("Nombre en mayúsculas:", nombre_completo)
print("Nombre en minúsculas:", nombre_completo.lower())
print("Nombre en mayúsculas:", nombre_completo.title())