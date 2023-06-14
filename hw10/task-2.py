# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    print(division)
    return division


def test_zero():
    with pytest.raises(ZeroDivisionError):
        all_division(2, 0)


@pytest.mark.smoke
def test_values_type_int():
    assert all_division(10, 2)


@pytest.mark.acceptance
def test_values_type_float():
    assert all_division(2.5, 0.2) == 12.5


def test_values_error():
    with pytest.raises(TypeError):
        all_division('sd', ['0', 1], {'key': 1})


def test_not_arguments():
    with pytest.raises(IndexError):
        all_division()
