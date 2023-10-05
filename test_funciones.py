import pytest
from funciones import *

# Temperatura promedio
@pytest.mark.parametrize("a,b,res",[
    (5,6,5.5),
    (8,4,6),
    (10,20,15)
])
def test_prom_temp(a,b,res):
    assert prom_temp(a,b)==res

# Chequeador de primos
@pytest.mark.parametrize("a,res",[
    (8, False),
    (9, False),
    (5, True),
    (13, True),
    (17, True),
    (25, False)
])
def test_prime_checker(a,res):
    assert prime_checker(a)==res

# Longitud de la primer palabra
@pytest.mark.parametrize("word,length",[
    ("   Hola como estas  ", 4),
    ("  Abc deD fAoasdaeE ", 3),
    ("hola amigoooo", 4)
])
def test_last_word_len(word,length):
    assert last_word_len(word)==length

# Contador de digitos en una lista
@pytest.mark.parametrize("num,digit,res",[
    ([3,2,3,4],3,2),
    ([3],4,0),
    ([5,5,5,4,2,2,5],5,4),
    ([5,5,5,4,2,2,5],2,2)
])
def test_frequency_digit_counter(num,digit,res):
    assert frequency_digit_counter(num,digit)==res