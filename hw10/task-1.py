# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random
import string


def for_generate_str(dictionary, lenletter):
    letter = ''
    for elem in range(lenletter):
        letter += random.choice(dictionary)
    return letter


def generate_random_name():
    while True:
        str1 = for_generate_str(string.ascii_lowercase, random.randint(1, 15))
        str2 = for_generate_str(string.ascii_lowercase, random.randint(1, 15))
        yield f'{str1} {str2}'


gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
