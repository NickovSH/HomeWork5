#Дано: текст (str).
# Задание: необходимо получить 2 словаря (популярности слов и популярности букв).
# Пример:
#  text = "hello, word of word", результат:
#      chars_popularity = {'h': 1, 'e': 1, 'l': 2, ..};
#      words_popularity = {'hello': 1, 'word': 2, 'of': 1}

def analysis_popularity():

    print('\nExercise 1 - Text analysis and popularitt')
    print('Введите строку')
    text_for_analysis = input()

    #Разбиваем строку на уникальные символы
    unique_letters = text_for_analysis.replace(' ', '').replace(',', '').replace('.', '').replace(';', '').replace(':', '')
    unique_letters = set(unique_letters)
    list_of_unique_letters = []

    #Создаем список уникальных букв
    for letter in unique_letters:
        list_of_unique_letters.append(letter)

    #Делим строку на слова
    split_text_for_analysis = text_for_analysis.split()

    #Создаем список уникальных слов
    list_of_unique_words = []
    for word in split_text_for_analysis:
        if word not in list_of_unique_words:
            list_of_unique_words.append(word)

    #Создаем словарь из ключей - уникальных букв и значений - количества букв

    values_for_letter_dict = []
    for i in range(len(list_of_unique_letters)):
        values_for_letter_dict.append(0)

    letter_dictionary = dict(zip(list_of_unique_letters, values_for_letter_dict))

    #Считаем количество букв в тексте
    for i in text_for_analysis:
        if i in letter_dictionary:
            letter_dictionary[i] += 1

    #Создаем словарь из ключей - уникальных слов и значений - количество слов

    values_for_word_dict = []
    for i in range(len(list_of_unique_words)):
        values_for_word_dict.append(0)

    word_dictionary = dict(zip(list_of_unique_words, values_for_word_dict))

    #Считаем количество уникальных слов
    for i in split_text_for_analysis:
        if i in word_dictionary:
            word_dictionary[i] += 1

    print('chars_popularity = ', letter_dictionary)
    print('words_popularity = ', word_dictionary)
