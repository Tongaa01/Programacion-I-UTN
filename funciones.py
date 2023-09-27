# Sumador de digitos
def digit_counter (counter):
    number_counter = 0
    for i in range (0, len(str(counter)), 1):
        number_counter = number_counter + int(str(counter)[i])
    return number_counter

