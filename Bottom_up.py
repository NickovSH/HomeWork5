# Дано: словарь ФИО - номер телефона(dict).
# Задание: получить новый словарь, инвертировав исходный, т.е. пары ключ - значение поменять местами (значение - ключ).
# Пример:
#  book = {'Petr': '546810', 'Katya': '241815'}, результат: {'546810': 'Petr', '241815': 'Katya'}


def reverse_key_value_in_dictionary():

    print('\nExercise 4 - Bottom up')

    #Словарь - телефонная книга
    dictionary_notebook = {'Иванов': 79641024784, 'Чебатков': 79684254201, 'Крючков': 79014538460,
                           'Трюфелев': 79603487201, 'Ключаев': 798742501234, 'Милославский': 79641036871}

    inverse_dictionary_notebook = {}

    #Изменение ключа и значения
    for key, value in dictionary_notebook.items():
        inverse_dictionary_notebook[value] = key


    print(inverse_dictionary_notebook)

