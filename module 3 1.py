# Вам необходимо написать 3 функции:
# Функция count_calls подсчитывающая вызовы остальных функций.
# Функция sring_infot принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
# Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке, False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
# Пункты задачи:
# Создать переменную calls = 0 вне функций.
# Создать функцию count_calls и изменять в ней значение переменной calls. Эта функция должна вызываться в остальных двух функциях.
# Создать функцию string_info с параметром string и реализовать логику работы по описанию.
# Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
# Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.
# # Вывести значение переменной calls на экран(в консоль).


calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    a = string
    a = len(string), string.upper(), string.lower()
    return a

def is_contains(string, list_to_search):
    count_calls()
    for i in list_to_search:
        if string.lower() in i.lower() or i.lower() in string.lower():
            return True
        else:
            return False



print(string_info('Vladivostok'))
print(string_info('Sevostopol'))
print(is_contains('Vladivostok', ['Vlad', 'vostok', 'VladIK']))
print(is_contains('Varvara', ['Masha', 'Denis', 'Varvar']))
print(calls)
