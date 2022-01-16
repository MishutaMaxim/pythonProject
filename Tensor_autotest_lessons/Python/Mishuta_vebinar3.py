# Написать функцию cash, где аргументы deposit – сумма вклада, persent – процент  годовых, years – срок вклада.
# Функция возвращает сумму, которая будет к указанному году
def cash(deposit, persent, years):
    for i in range(years):
        deposit += deposit * (persent / 100)
    return deposit


# Напишите функцию, которая проверяет является ли число палиндромом. Палиндром — число,
# одинаково читающееся в обоих направлениях. Например: 121, 1331
def is_palindrom(number):
    number = str(number)
    if number == number[::-1]:
        return True
    else:
        return False


# Вывести список простых чисел до 1000. Число простое, если оно имеет только 2 делителя (1 и само себя).
def simple_numbers():
    for number in range(1, 1001):
        count = 0
        for delitel in range(1, number + 1):
            if number % delitel == 0:
                count += 1
        if count == 2:
            print(number)


# Напишите функцию, которая подсчитывает количество счастливых шестизначных билетов. Билеты начинаются с 000000 и
# заканчиваются 999999. Счастливым считается билет, если сумма первых трех значений, равна сумме вторых трёх (
# Например: 927864, 123006, 002110 и т.д.)
def count_lucky_ticket():
    count_lucky = 0
    for n in range(1000000):
        n = str(n).zfill(6)
        if int(n[0]) + int(n[1]) + int(n[2]) == int(n[3]) + int(n[4]) + int(n[5]):
            count_lucky += 1
    return count_lucky


# Напишите функцию. На вход подается строка (текст), на выходе должен быть словарь, где ключ – это слово,
# а значение – число: сколько раз данное слово повторилось в тексте (регистр не имеет значения).
# Например:
# """Мело, мело по всей земле
# Во все пределы.
# Свеча горела на столе,
# Свеча горела.
#
# Метель лепила на стекле
# Кружки и стрелы.
# Свеча горела на столе,
# Свеча горела."""
#
# {‘Мело’:2, ‘Свеча’: 4, ‘горела’: 4, ‘на’: 3…}
def word_counter(import_text):
    # Убираем из строки лишне, оставляем только слова в нижнем регистре
    words = import_text.replace('.', '').replace(',', '').replace('\n', '').lower()
    result = {}
    # Циклом перебираем все слова в строке
    for word in words.split():
        # Если слово не встречается в словаре - добавляем слово ключ и количество его повторений в строке
        if word not in result:
            result.update({word: words.count(word)})
    # Возвращаем словарь
    return result


string = 'Мело, мело по всей земле Во все пределы. Свеча горела на столе, Свеча горела. ' \
         'Метель лепила на стекле Кружки и стрелы. Свеча горела на столе, Свеча горела.'
