# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest


class TestExample:
    @pytest.mark.usefixtures('for_time')
    def test_1(self):
        print('Запуск 1 теста')

    @pytest.mark.usefixtures('for_time_run')
    def test_2(self):
        print('Запуск 2 теста')
