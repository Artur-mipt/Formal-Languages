from Rule import Rule
from Situation import Situation


class Earley:
    rules = []  # массив правил в грамматике
    situations_dict = {}  # словарь множеств ситуаций, situations_dict[i] - i-ое множество
    word = str  # слово, которое нужно распознать

    def __init__(self, word):
        # добавляем (S# -> .S; 0) в D[0], инициализируем все D[i]
        sit = Situation('S#', 'S', 0, 0)
        self.situations_dict[0] = set()
        self.situations_dict[0].add(sit)
        for i in range(1, len(word) + 1):
            self.situations_dict[i] = set()

        self.word = word

    # добавление правил грамматики
    def add_rule(self, rule):
        self.rules.append(rule)

    # добавление ситуации в конкретное множество ситуаций
    def add_situation(self, situation, list_number):
        is_already_added = False
        for sit in self.situations_dict[list_number]:
            if (sit.to == situation.to and sit.out == situation.out
                    and sit.point == situation.point and sit.ind == situation.ind):
                is_already_added = True
        if not is_already_added:
            self.situations_dict[list_number].add(situation)

    # функция Predict
    def predict(self, list_number):
        situations_to_insert = []
        for situation in self.situations_dict[list_number]:
            if situation.point < len(situation.to):
                unterminal = situation.to[situation.point]  # смотрим нетерминальный символ после точки
                for rule in self.rules:
                    if rule.out == unterminal:  # что выводится из этого нетерминала
                        sit = Situation(unterminal, rule.to, list_number, 0)
                        situations_to_insert.append(sit)

        for sit in situations_to_insert:
            self.add_situation(sit, list_number)

    # функция Scan
    def scan(self, list_number, symbol):
        for situation in self.situations_dict[list_number]:
            if situation.to[situation.point] == symbol:
                sit = Situation(situation.out, situation.to, situation.ind, situation.point + 1)
                self.add_situation(sit, list_number + 1)

    # функция Complete
    def complete(self, list_number):
        situations_to_insert = []
        for situation in self.situations_dict[list_number]:
            list_number_2 = situation.ind
            if situation.point == len(situation.to):
                for situation_2 in self.situations_dict[list_number_2]:
                    sit = Situation(situation_2.out, situation_2.to, situation_2.ind, situation_2.point + 1)
                    situations_to_insert.append(sit)

        for sit in situations_to_insert:
            self.add_situation(sit, list_number)

    # распознается ли слово word грамматикой
    def get_answer(self):
        prev_len = len(self.situations_dict[0])
        self.predict(0)
        self.complete(0)
        new_len = len(self.situations_dict[0])
        while new_len != prev_len:
            prev_len = new_len
            self.predict(0)
            self.complete(0)
            new_len = len(self.situations_dict[0])

        for i in range(1, len(self.word) + 1):
            self.scan(i - 1, self.word[i - 1])
            prev_len = len(self.situations_dict[i])
            self.predict(i)
            self.complete(i)
            new_len = len(self.situations_dict[i])
            while new_len != prev_len:
                prev_len = new_len
                self.predict(i)
                self.complete(i)
                new_len = len(self.situations_dict[i])

        for situation in self.situations_dict[len(self.word)]:
            if situation.out == 'S#' and situation.to == 'S' and situation.ind == 0 and situation.point == 1:
                return 'YES'

        return 'NO'
