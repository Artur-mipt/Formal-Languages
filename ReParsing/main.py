# -*- coding: utf-8 -*-
inf_const = float('inf')


# в случае сложения или конкатенация нам надо выкинуть последние два
# элемента из всех стэков и запомнить их значения
def pop_2_elements(d):
    c2 = d['count_x'].pop()
    c1 = d['count_x'].pop()
    p2 = d['pref_x'].pop()
    p1 = d['pref_x'].pop()
    s2 = d['suff_x'].pop()
    s1 = d['suff_x'].pop()
    o2 = d['only_x'].pop()
    o1 = d['only_x'].pop()
    mx2 = d['max_len'].pop()
    mx1 = d['max_len'].pop()
    mn2 = d['min_len'].pop()
    mn1 = d['min_len'].pop()
    return [c1, c2, p1, p2, s1, s2, o1, o2, mx1, mx2, mn1, mn2]


def equal_x(d):
    d['count_x'].append(1)
    d['pref_x'].append(1)
    d['suff_x'].append(1)
    d['only_x'].append(True)
    d['max_len'].append(1)
    d['min_len'].append(1)


def just_letter(d):
    d['count_x'].append(0)
    d['pref_x'].append(0)
    d['suff_x'].append(0)
    d['only_x'].append(False)
    d['max_len'].append(1)
    d['min_len'].append(1)


def empty_word(d):
    d['count_x'].append(0)
    d['pref_x'].append(0)
    d['suff_x'].append(0)
    d['only_x'].append(False)
    d['max_len'].append(0)
    d['min_len'].append(0)


def plus(d):
    info = pop_2_elements(d)
    d['count_x'].append(max(info[0], info[1]))
    d['pref_x'].append(max(info[2], info[3]))
    d['suff_x'].append(max(info[4], info[5]))
    d['only_x'].append(info[6] or info[7])
    d['max_len'].append(max(info[8], info[9]))
    d['min_len'].append(min(info[10], info[11]))


def concat(d):
    info = pop_2_elements(d)
    d['count_x'].append(max(max(info[0], info[1]), info[3] + info[4]))
    if info[10] > 0 and info[11] > 0:  # если оба слова непустые
        d['only_x'].append(info[6] and info[7])
    else:  # если хотя бы одно м.б. пустым
        d['only_x'].append(info[6] or info[7])
    d['max_len'].append(info[8] + info[9])
    d['min_len'].append(info[10] + info[11])
    if info[6] and info[7]:
        d['pref_x'].append(info[8] + info[9])
        d['suff_x'].append(info[8] + info[9])
    else:
        if info[6]:  # второе слово может состоять только из x
            d['pref_x'].append(info[2] + info[3])
        else:
            if info[10] == 0:  # первое слово м.б. пустым
                d['pref_x'].append(max(info[2], info[3]))
            else:  # первое слово всегда непустое
                d['pref_x'].append(info[2])
        if info[7]:  # второе слово может состоять только из x
            d['suff_x'].append(info[5] + info[4])
        else:
            if info[11] == 0:  # если второе слово из конкатенации м.б. пустым
                d['suff_x'].append(max(info[4], info[5]))
            else:  # второе слово всегда непустое
                d['suff_x'].append(info[5])


def star(d):
    info = d['count_x'].pop()
    tmp = d['suff_x'][len(d['suff_x']) - 1]
    tmp += d['pref_x'][len(d['pref_x']) - 1]
    d['count_x'].append(max(info, tmp))
    d['min_len'].pop()
    d['min_len'].append(0)
    d['max_len'].pop()
    d['max_len'].append(inf_const)


def get_answer(re, x):

    if not 'a' <= x <= 'c':
        return "Error"

    d = {}
    d['count_x'] = []  # max k : x^k является подстрокой слов, задаваемых регуляркой
    d['pref_x'] = []   # max k: x^k является префиксом слов, задаваемых регуляркой
    d['suff_x'] = []   # max k: x^k является суффиксом слов, задаваемых регуляркой
    d['only_x'] = []   # true - если слово, задаваемое регуляркой, может состоять только из букв x
    d['max_len'] = []  # min k: слово, задаваемое регуляркой, имеет длину k
    d['min_len'] = []  # max k: слово, задаваемое регуляркой, имеет длину k

    for c in re:
        if c == x:  # если символ совпадает с буквой x
            equal_x(d)
        else:
            if 'a' <= c <= 'c':  # если символ - буква, но не x
                just_letter(d)
            elif c == '1':
                empty_word(d)
            elif c == '+':  # если символ - операция "или"
                if len(d['count_x']) < 2:
                    return "Error"
                plus(d)
            elif c == '.':  # если символ - операция конкатенации
                if len(d["count_x"]) < 2:
                    return "Error"
                concat(d)
            elif c == '*':  # если символ - звезда Клини
                if len(d["count_x"]) < 1:
                    return "Error"
                # может ли регулярка состоять из ненулевого числа букв x
                flag_only_x = d['only_x'][len(d['only_x']) - 1]
                if flag_only_x:
                    return "INF"
                star(d)
            else:  # если символ неккоректен
                return "Error"

    if len(d["count_x"]) > 1:  # если на стэке осталось более 1 элемента
        return "Error"

    return d["count_x"][0]


def main():
    re = input()
    x = input()

    print(get_answer(re, x))


main()
