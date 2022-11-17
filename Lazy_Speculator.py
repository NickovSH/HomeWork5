# Дано: словарь банк - курс доллара (dict).
# Задание: определить банк и курс покупки валюты с наиболее привлекательным предложением.
# Пример:
#  rates = {'Sberbank': 55.8, 'VTB24': 53.91}, результат: VTB24 -> 53.91

def bank_selection():

    print('\nExercise 3 - Lazy Speculator')

    #Курсы доллара на 17.11.2022 в Томских банках
    exchange_rate_dictionary = {'Sberbank': 59.53, 'VTB': 60.3, 'Gazprombank': 62.3, 'Rosselkhozbank': 59.6,
                                'Promsvyazbank': 59.41, 'Sovcombank': 59.5, 'Raiffeisenbank': 54}

    #Поиск минимального значения курса в словаре
    min_exchange_rate_value = min(exchange_rate_dictionary.values())
    list_bank = []

    #Поиск всех банков с минимальным значением курса
    for key in exchange_rate_dictionary:
        if exchange_rate_dictionary[key] == min_exchange_rate_value:
            list_bank.append(key)

    print('Лучший курс у банка/банков: ', list_bank, '->', min_exchange_rate_value)