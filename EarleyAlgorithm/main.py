from Earley import Earley
from Rule import Rule


def main():

    print('Введите кол-во правил в грамматике\n')
    n = int(input())

    print('Введите правила грамматики в формате S -> aB\n')
    rules = []
    for i in range(0, n):
        s = input()
        parts = s.split(' ')
        rules.append(Rule(parts[0], parts[2]))
    rules.append(Rule('S#', 'S'))

    print('Введите слово, которое нужно распознать\n')
    word = input()

    earley = Earley(word)
    for rule in rules:
        earley.add_rule(rule)

    print('Answer: ', earley.get_answer())


main()
