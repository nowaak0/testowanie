import random
from unittest import mock
import unittest

# Prosta funkcja, która wykorzystuje funkcję is_prime
def get_random_prime():
    n = random.randint(1, 100)
    if is_prime(n):
        return n
    return None

# Funkcja do atakowania
def external_data_fetch():
    return random.choice([17, 20, 29, 30])

def get_prime_from_external_data():
    data = external_data_fetch()
    return is_prime(data)
