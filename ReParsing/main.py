

# в случае сложения или конкатенация нам надо выкинуть последние два
# элемента из всех стэков и запомнить их значения
def pop_2_elements(count_x, pref_x, suff_x, only_x):
    if len(count_x) < 2:
        print("Re is incorrect")
        exit(0)

    c2 = count_x.pop()
    c1 = count_x.pop()
    p2 = pref_x.pop()
    p1 = pref_x.pop()
    s2 = suff_x.pop()
    s1 = suff_x.pop()
    o2 = only_x.pop()
    o1 = only_x.pop()
    return [c1, c2, p1, p2, s1, s2, o1, o2]


def equal_x(count_x, pref_x, suff_x, only_x):
    count_x.append(1)
    pref_x.append(1)
    suff_x.append(1)
    only_x.append(True)


def just_letter(count_x, pref_x, suff_x, only_x):
    count_x.append(0)
    pref_x.append(0)
    suff_x.append(0)
    only_x.append(False)


def plus(count_x, pref_x, suff_x, only_x):
    info = pop_2_elements(count_x, pref_x, suff_x, only_x)
    count_x.append(max(info[0], info[1]))
    pref_x.append(max(info[2], info[3]))
    suff_x.append(max(info[4], info[5]))
    only_x.append(info[6] or info[7])


def concat(count_x, pref_x, suff_x, only_x):
    info = pop_2_elements(count_x, pref_x, suff_x, only_x)
    count_x.append(max(max(info[0], info[1]), info[4] + info[2]))
    pref_x.append(info[2])
    suff_x.append(info[5])
    only_x.append(info[6] and info[7])


def star(count_x, pref_x, suff_x, only_x):
    if only_x[len(only_x) - 1] is True:
        print("INF")
        exit(0)

    info = count_x.pop()
    count_x.append(max(info, suff_x[len(suff_x) - 1] + pref_x[len(pref_x) - 1]))


def main():
    re = input()
    x = input()

    if not 'a' <= x <= 'c':
        print("Symbol x is incorrect")
        exit(0)

    count_x = []  # max k : x^k является подстрокой слов, задаваемых регуляркой
    pref_x = []   # max k: x^k является префиксом слов, задаваемых регуляркой
    suff_x = []   # max k: x^k является суффиксом слов, задаваемых регуляркой
    only_x = []   # true - если слово, задаваемое регуляркой, может состоять только из букв x

    for c in re:
        if c == x:  # если символ совпадает с буквой x
            equal_x(count_x, pref_x, suff_x, only_x)
        else:
            if 'a' <= c <= 'c':  # если символ - буква, но не x
                just_letter(count_x, pref_x, suff_x, only_x)
            elif c == '+':  # если символ - операция "или"
                plus(count_x, pref_x, suff_x, only_x)
            elif c == '.':  # если символ - операция конкатенации
                concat(count_x, pref_x, suff_x, only_x)
            elif c == '*':  # если символ - звезда Клини
                star(count_x, pref_x, suff_x, only_x)
            else:  # если символ неккоректен
                print("Re is incorrect")
                exit(0)

    if len(count_x) > 1:  # если на стэке осталось более 1 элемента
        print("Re is incorrect")
        exit(0)

    print(count_x[0])


main()
