# -*- coding: utf-8 -*-
from main import get_answer


# тест на все виды ошибок
def error_test():
    answers = []

    answers.append(get_answer('ab.', 'd'))  # неккоректный символ x
    answers.append(get_answer('ab', 'a'))  # после разбора регулярки на стеке больше одного эл.
    answers.append(get_answer('ab..', 'a'))  # при применении бинарной операции на стеке 1 эл.
    answers.append(get_answer('+', 'a'))  # при применении бинарной операции на стеке 0 эл.
    answers.append(get_answer('*', ''))  # при применении унарной операции на стеке 0 эл.
    answers.append(get_answer('ad.*', 'a'))  # неккоректный символ в регулярке

    for answer in answers:
        if answer != 'Error':
            return "error_test failed"

    return "error_test passed"


# тест на ответ INF
def inf_test():
    answers = []

    answers.append(get_answer('a*', 'a'))
    answers.append(get_answer('ab+*', 'a'))
    answers.append(get_answer('ab+*a+', 'a'))

    for answer in answers:
        if answer != 'INF':
            return "inf_test failed"

    return "inf_test passed"


# тест на обычные численные ответы
def number_test():
    flag = True

    if get_answer('abc..ab.+', 'c') != 1:
        flag = False
    if get_answer('abc..ab.+', 'a') != 1:
        flag = False
    if get_answer('abc..ab.+*', 'a') != 1:
        flag = False
    if get_answer('aba..*', 'a') != 2:
        flag = False

    if flag:
        return "number_test passed"
    return "number_test failed"


print(error_test())
print(inf_test())
print(number_test())
