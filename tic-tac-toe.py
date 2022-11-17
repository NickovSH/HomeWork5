# Дано: список (list) строк, где "X" и "O" - это отметки игроков и "." - это пустая клетка.
# Задание.
# Крестики-нолики - это игра для двух игроков (Х и О), которые расставляют эти знаки на 3х3 поле. Игрок, который
# сумел разместить три своих знака в любой горизонтали, вертикали или диагонали -- выигрывает.
# Но сейчас мы не будем играть в эту игру. Вы будете судить игру, и оценивать результат. Вам дан результат
# игры, и вы должны решить, кто победил или что это ничья. Ваша программа должна вернуть "X" если победил
# Х-игрок и "О" если победил О-игрок. В случае ничьи, результат должен быть "D".

#Функция для ввода поля
def input_fields():
    print('\nExercise 6 - tic-tac-toe')
    print('Введите первую строку через пробел, пример: X O . ')
    line1_fields = input()
    line1_fields = line1_fields.split()
    print('Введите вторую строку через пробел, пример: X O . ')
    line2_fields = input()
    line2_fields = line2_fields.split()
    print('Введите третью строку через пробел, пример: X O . ')
    line3_fields = input()
    line3_fields = line3_fields.split()

    search_for_a_winner(line1_fields, line2_fields, line3_fields)

#Функция поиска победителя
def search_for_a_winner(line1_fields, line2_fields, line3_fields):

    fields = [line1_fields,
              line2_fields,
              line3_fields]

    X_count = False
    O_count = False
    point_count = 0

    #Проверка по горизонтали
    for line in fields:
        if line[0] == line[1] == line[2] == 'X':
            X_count = True
        elif line[0] == line[1] == line[2] == 'O':
            O_count = True

    # Проверка по вертикали
    for i in range(len(fields)):
        if line1_fields[i] == line2_fields[i] == line3_fields[i] == 'X':
            X_count = True
        elif line1_fields[i] == line2_fields[i] == line3_fields[i] == 'O':
            O_count = True

    #Проверка по диагонали X
    if line1_fields[0] == line2_fields[1] == line3_fields[2] == 'X':
        X_count = True
    elif line1_fields[2] == line2_fields[1] == line3_fields[0] == 'X':
        X_count = True

    #Проверка по диагонали O
    if line1_fields[0] == line2_fields[1] == line3_fields[2] == 'O':
        O_count = True
    elif line1_fields[2] == line2_fields[1] == line3_fields[0] == 'O':
        O_count = True

    #Итоговый результат
    if ((X_count and O_count) == True) and ((X_count and O_count) == False):
        print('Результат: D')
    elif X_count == True:
        print('Результат: X')
    else:
        print('Результат: O')

#Основная функция
def main():
    input_fields()

main()


