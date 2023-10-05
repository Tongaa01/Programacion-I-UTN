import math

# Sumador de digitos
def digit_counter (counter):
    number_counter = 0
    for i in range (0, len(str(counter)), 1):
        number_counter = number_counter + int(str(counter)[i])
    return number_counter

# Promedio de temperatura
def prom_temp (min_temp, max_temp):
    prom = (min_temp + max_temp)/2
    return prom

# Números primos
def prime_checker (num):
    is_prime = True
    for i in range (2, num, 1):
        if num%i==0:
            is_prime = False
    return is_prime

# Longitud de la ultima palabra
def last_word_len (phrase):
    phrase = list(phrase)
    while True:
        if phrase[0]==" ":
            phrase.remove(phrase[0])
        else:
            break
    phrase = "".join(phrase)
    word_len = len(phrase[0:phrase.find(" ")])
    return word_len

# Contador de frecuencia del digito
def frequency_digit_counter(num, digit):
    counter = num.count(digit)
    return counter