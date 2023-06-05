# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
with open('test_file/task3.txt', 'r', encoding='utf-8') as file:
    sales = file.readlines()
    sum_buy_array = []
    sum_one_buy = 0
    for elem in sales:
        if elem[0].isdigit():
            sum_one_buy += int(elem)
        else:
            sum_buy_array.append(sum_one_buy)
            sum_one_buy = 0
    sum_buy_array = sorted(sum_buy_array)
    three_most_expensive_purchases = (sum_buy_array[len(sum_buy_array) - 1]
                                      + sum_buy_array[len(sum_buy_array) - 2] + sum_buy_array[len(sum_buy_array) - 3])
assert three_most_expensive_purchases == 202346
