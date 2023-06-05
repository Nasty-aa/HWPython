# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


# Здесь пишем код
'''
Открываем task1_data.txt, пробегаемся по всем символам и если елемент не число записываем в новую переменную
'''


with open('test_file/task1_data.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    new_text = ''
    for elem in text:
        if not elem.isdigit():
            new_text += elem
'''
Создаем/Открываем task1_answer.txt, записываем результат
'''
with open("test_file/task1_answer.txt", 'w', encoding='utf-8') as file_answer:
    file_answer.write(new_text)

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
