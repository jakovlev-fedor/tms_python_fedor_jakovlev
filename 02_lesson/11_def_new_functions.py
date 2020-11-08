""""""

"""
# 01-------------------------
Написать функцию, которая принимает 2 числа и возвращает их сумму

"""


def sum_two_nums(number_01, number_02):

    total = number_01 + number_02

    return total


# print(sum_two_nums(33, 66))


"""
# 02-------------------------
Написать функцию, которая принимает 1 число и возвращает его произведение на 4

"""


def multiply_by_four(number_01):

    multiplied = number_01 * 4

    return multiplied


# print(multiply_by_four(25))


"""
# 03-------------------------
Написать функцию, которая принимает 3 числа, и их сумму делит на 3

"""


def mean_value_in_trinity(number_01, number_02, number_03):

    total = sum([number_01, number_02, number_03])
    result = total / 3

    return result


# print(mean_value_in_trinity(30, 60, 90))


"""
# 04-------------------------
Написать функцию, которая не принимает аргументов, но возвращает 7

"""


def get_seven():

    SEVEN = 7

    return SEVEN


# print(get_seven())


"""
# 05-------------------------
Написать функцию, которая принимает 1 число и возвращает его остаток от деления на 5

"""


def get_reminder_from_division_by_5(number_01):

    reminder = number_01 % 5

    return reminder


# print(get_reminder_from_division_by_5(25)) # zero expected


"""
# 06-------------------------
Написать функцию, которая принимает 2 числа и возвращает словарь 
который содержит эти 2 числа и их сумму. 
Ключи для чисел придумать самостоятельно.

"""


def make_dictionary(number_01, number_02):

    total = number_01 + number_02
    dictionary_01 = {'1st': number_01, '2nd': number_02, 'Sum': total}

    return dictionary_01


# print(make_dictionary(23, 32))


"""
# 07-------------------------
Написать функцию, которая принимает список, 
проверяет есть ли в нём число 8 или число 4. 
Возвращает истину или ложь.

"""


def is_contains_8_or_4(list_01):

    result = (8 in list_01) or (4 in list_01)

    return result


list_true = [8, 0, 5, 1]
list_false = [7, 3, 0, 5, 1]

# print(is_contains_8_or_4(list_true))
# print(is_contains_8_or_4(list_false))


"""
# 08-------------------------
Написать функцию, которая принимает 2 списка
и делит 2-е число первого списка на первое число второго списка. 
Результат деления возвращает.

"""


def complex_lists_manipulation(list_01, list_02):

    num_01 = list_01[1]
    num_02 = list_02[0]
    result = num_01 / num_02

    return result


list1 = [8, 4, 0, 5, 1]
list2 = [8, 4, 0, 5, 1]

# print(complex_lists_manipulation(list1, list2))


"""
# 09-------------------------
Написать функцию. Принимает строку и 
заменяет в ней все пробелы на строку "privet"

"""


def flood_string_with_privet(string_01):

    result = string_01.replace(' ', 'privet')

    return result


str1 = ' - - - '

# print(flood_string_with_privet(str1))


"""
# 10-------------------------
Написать функцию которая принимает строку и возвращает 2-е слово. 
Предполагается что строка содержит слова разделенные пробелом.

"""


def get_second_word_from_string(string_01):

    list_01 = string_01.split(' ')
    second_word = list_01[1]

    return second_word


str2 = 'one two three four '

# print(get_second_word_from_string(str2))


"""
# 11-------------------------
Написать функцию принимающую список и меняет первый элемент на 4. 
Возвращает измененный список.

"""


def mutate_to_four(list_01):

    list_01[0] = 4

    return list_01


list11 = [8, 4, 0, 5, 1]
# print(mutate_to_four(list11))


"""
# 12-------------------------
Написать функцию принимающую словарь и меняет значение под ключём 'A' на 65. 
Возвращает измененный словарь.

"""


def change_65_value_to_a(dictionary_01):

    dictionary_01['A'] = 65

    return dictionary_01


ascii_code_dictionary = {
    'A': None,
    'B': 66,
    'C': 67,
}

# print(change_65_value_to_a(ascii_code_dictionary))


"""
# 13-------------------------
Написать функцию принимающую словарь 
и возвращает этот же словарь но уже без ключа 'b'.

"""


def delete_b_key(dictionary_01):

    del dictionary_01['b']

    return dictionary_01


dict13 = {
    'a': 1,
    'b': 2,
    'c': 3
}

# print(delete_b_key(dict13))


"""
# 14-------------------------
Написать функцию принимающую список цифр 
и добавляющую ко второму элементу 33 и возвращает список.

"""


def add_33_to_second_item(list_01):

    list_01[1] = list_01[1] + 33

    return list_01


list14 = [11, 11, 11]
# print(add_33_to_second_item(list14))


"""
# 15-------------------------
Написать функцию принимающую список, 
добавить к этому списку новый элемент 
который будет равен сумме первого и последнего элемента этого списка. 
Получить последний элемент списка можно так: ls[-1]

"""


def bind_tails(list_01):

    new_item = list_01[0] + list_01[-1]
    list_01.append(new_item)

    return list_01


list15 = [10, 20, 30]
# print(bind_tails(list15))


"""
# 16-------------------------
Написать функцию принимающую словарь 
и добавляет к словарю ключ 'c' 
который содержит сумму числа под ключём 'a' и 45.

"""


def add_45_value(dictionary_01):

    dictionary_01['c'] = dictionary_01['a'] + 45

    return dictionary_01


dict16 = {
    'a': 0,
    'b': 2,
}


# print(add_45_value(dict16))


"""
# 17-------------------------
Написать функцию которая принимает список 
и делает первые два элемента одинаковыми.

"""


def equalize_first_two_elements(list_01):

    list_01[1] = list_01[0]

    return list_01


list17 = [1, 2, 3, 4, 5]
# print(equalize_first_two_elements(list17))


"""
# 18-------------------------
Написать функцию которая принимает словарь и число, 
удаляет ключ 'a' и добавляет ключ 'c' 
который должен содержать значение равное этому числу.

"""


def remove_add_set(dictionary_01, number_01):

    del dictionary_01['a']
    dictionary_01['c'] = number_01

    return dictionary_01


dict18 = {
    'a': 97,
    'b': 98,
    'd': 100
}

# print(remove_add_set(dict18, 99))


"""
# 19-------------------------
Написать функцию которая принимает список 
и возвращает список который содержит только первый и последний элемент списка. 
Получить последний элемент списка можно так: ls[-1]

"""


def get_first_and_last(list_01):

    # list_02 = list_01[0], list_01[-1]

    indices_to_access = [0, -1]
    mapped_items = map(list_01.__getitem__, indices_to_access)
    list_02 = list(mapped_items)

    return list_02


list19 = ['first', 'middle', 'last']
# print(get_first_and_last(list19))


"""
# 20-------------------------
Написать функцию которая принимает словарь 
и возвращает список содержащий значения по ключам 'b' и 'm'.

"""


def get_b_and_m_values(dictionary_01):

    list_01 = [
        dictionary_01['b'],
        dictionary_01['m']
    ]

    return list_01


dict20 = {
    'a': 97,
    'b': 98,
    'c': 99,
    'd': 100,
    'm': 109,
    'n': 110,
    'o': 111
}

# print(get_b_and_m_values(dict20))


"""
# 21-------------------------
Написать функцию которая принимает число и список 
и добавляет его в начало списка.

"""


def add_number_to_the_list_beginning(number_01, list_01):

    list_01 = [number_01] + list_01

    return list_01


list21 = [12, 34, 45, 56, 67]
# print(add_number_to_the_list_beginning(99, list21))

"""
# 22-------------------------
Написать функцию принимающую строку, 
состоящую из слов разделенных пробелами.
Функция должна возвращать сколько в строке слов.

"""


def word_counter(string_01):
    word_list = string_01.split(' ')
    counter = len(word_list)

    return counter


string22 = 'one two three four five'
# print(word_counter(string22))


"""
# 23-------------------------
Написать функцию принимающую строку состоящую ровно из двух слов, разделенных пробелом.
Функция должна возвращать строку аналогичную входящей, но только слова должны поменяться местами.
Пример:
>>> fn("республика беларусь")
"беларусь республика"

"""


def swap_two_words(two_words):

    two_words_splitted_list = two_words.split(' ')
    two_words_swapped_list = [
        two_words_splitted_list[1],
        two_words_splitted_list[0]
    ]
    two_words_swapped = ' '.join(two_words_swapped_list)

    return two_words_swapped

# print(swap_two_words('zig zag'))
