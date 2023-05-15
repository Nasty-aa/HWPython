# Задача со ЗВЁЗДОЧКОЙ. Решать НЕ обязательно.
# Программа получает на вход натуральное число num.
# Программа должна вывести другое натуральное число, удовлетворяющее условиям:
# Новое число должно отличаться от данного ровно одной цифрой
# Новое число должно столько же знаков как исходное
# Новое число должно делиться на 3
# Новое число должно быть максимально возможным из всех таких чисел
# Например (Ввод --> Вывод) :
#
# 379 --> 879
# 15 --> 75
# 4974 --> 7974

def max_division_by_3(num):
    num_array = []
    num1 = num
    max_num = num
    while num1 > 0:
        num_array.append(num1 % 10)
        num1 = num1 // 10
    num_array_len = len(num_array)
    num_array.reverse()
    if num_array_len > 0:
        while num_array_len > 0:
            num_array_copy = num_array[len(num_array) - num_array_len]
            while num_array[len(num_array) - num_array_len] < 10:
                num2 = int(''.join(map(str, num_array)))
                if num2 % 3 == 0 and max_num < num2:
                    max_num = num2
                num_array[len(num_array) - num_array_len] += 1
            num_array[len(num_array) - num_array_len] = num_array_copy
            num_array_len -= 1
    else:
        while num < 10:
            if num % 3 == 0 and max_num < num:
                max_num = num
            num += 1
    print(max_num)
    new_num = max_num
    return new_num

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    379, 810, 981, 4974, 996, 9000, 15, 0, 9881, 9984, 9876543210, 98795432109879543210
]

test_data = [
    879, 870, 987, 7974, 999, 9900, 75, 9, 9981, 9987, 9879543210, 98798432109879543210
]


for i, d in enumerate(data):
    assert max_division_by_3(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')