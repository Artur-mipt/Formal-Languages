# -*- coding: utf-8 -*-
from main import get_answer


# тест на все виды ошибок
def error_test():
    assert(get_answer('ab.', 'd')) == 'Error'  # неккоректный символ x
    assert(get_answer('ab', 'a')) == 'Error'  # после разбора регулярки на стеке больше одного эл.
    assert(get_answer('ab..', 'a')) == 'Error'  # при применении бинарной операции на стеке 1 эл.
    assert(get_answer('+', 'a')) == 'Error'  # при применении бинарной операции на стеке 0 эл.
    assert(get_answer('*', '')) == 'Error'  # при применении унарной операции на стеке 0 эл.
    assert(get_answer('ad.*', 'a')) == 'Error'  # неккоректный символ в регулярке

    return "error_test passed"


# тест на ответ INF
def inf_test():
    assert(get_answer('a*', 'a')) == 'INF'
    assert(get_answer('ab+*', 'a')) == 'INF'
    assert(get_answer('ab+*a+', 'a')) == 'INF'

    return "inf_test passed"


# тест на обычные численные ответы
def number_test():
    assert(get_answer('abc..ab.+', 'c')) == 1
    assert(get_answer('abc..ab.+', 'a')) == 1
    assert(get_answer('abc..ab.+*', 'a')) == 1
    assert(get_answer('aba..*', 'a')) == 2
    assert(get_answer('baa..ab.*aab....', 'a')) == 4

    return "number_test passed"


# тест на регулярки с пустым словом
def empty_word_test():
    assert(get_answer('a1a..', 'a')) == 2
    assert(get_answer('aa1..', 'a')) == 2
    assert(get_answer('a1+', 'a')) == 1
    assert(get_answer('1a+', 'a')) == 1
    assert(get_answer('11+', 'a')) == 0
    assert(get_answer('abc1...ab.+', 'c')) == 1
    assert(get_answer('abc..ab1..+', 'a')) == 1
    assert(get_answer('abc..ab.+1+*', 'a')) == 1
    assert(get_answer('ab.1+*', 'a')) == 1
    assert(get_answer('aa.1+*', 'a')) == 'INF'
        
    return "empty_word_test passed"


print(error_test())
print(inf_test())
print(number_test())
print(empty_word_test())
