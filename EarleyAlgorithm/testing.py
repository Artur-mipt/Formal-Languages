from Earley import Earley
from Rule import Rule
from Situation import Situation


def predict_test():
    earley = Earley('a')
    earley.rules = [Rule('S#', 'S'), Rule('S', 'a')]
    earley.situations_dict[0] = set()
    earley.situations_dict[0].add(Situation('S#', 'S', 0, 0))
    earley.predict(0)

    is_added = False
    to_add = Situation('S', 'a', 0, 0)
    for sit in earley.situations_dict[0]:
        if (sit.input == to_add.input and sit.output == to_add.output
                and sit.point == to_add.point and sit.ind == to_add.ind):
            is_added = True

    assert is_added is True
    print('Predict test passed\n')


def scan_test():
    earley = Earley('a')
    earley.rules = [Rule('S#', 'S'), Rule('S', 'a')]
    earley.situations_dict[0] = set()
    earley.situations_dict[1] = set()
    earley.situations_dict[0].add(Situation('S#', 'S', 0, 0))
    earley.situations_dict[0].add(Situation('S', 'a', 0, 0))
    earley.scan(0, 'a')

    is_added = False
    to_add = Situation('S', 'a', 0, 1)
    for sit in earley.situations_dict[1]:
        if (sit.input == to_add.input and sit.output == to_add.output
                and sit.point == to_add.point and sit.ind == to_add.ind):
            is_added = True

    assert is_added is True
    print('Scan test passed\n')


def complete_test():
    earley = Earley('a')
    earley.rules = [Rule('S#', 'S'), Rule('S', 'a')]
    earley.situations_dict[0] = set()
    earley.situations_dict[1] = set()
    earley.situations_dict[0].add(Situation('S#', 'S', 0, 0))
    earley.situations_dict[0].add(Situation('S', 'a', 0, 0))
    earley.situations_dict[1].add(Situation('S#', 'S', 0, 1))
    earley.complete(1)

    is_added = False
    to_add = Situation('S#', 'S', 0, 1)
    for sit in earley.situations_dict[1]:
        if (sit.input == to_add.input and sit.output == to_add.output
                and sit.point == to_add.point and sit.ind == to_add.ind):
            is_added = True

    assert is_added is True
    print('Complete test passed\n')


def get_answer_test():
    earley = Earley('a')
    earley.rules = [Rule('S#', 'S'), Rule('S', 'a')]
    assert(earley.get_answer()) == 'YES'

    earley = Earley('ab')
    earley.rules = [Rule('S#', 'S'), Rule('S', 'aA'), Rule('A', 'b')]
    assert (earley.get_answer()) == 'YES'

    earley = Earley('ab')
    earley.rules = [Rule('S#', 'S'), Rule('S', 'aA'), Rule('A', 'b')]
    assert (earley.get_answer()) == 'YES'

    earley = Earley('ac')
    earley.rules = [Rule('S#', 'S'), Rule('S', 'aA'), Rule('A', 'b')]
    assert (earley.get_answer()) == 'NO'

    print("Answer test passed")


predict_test()
scan_test()
complete_test()
get_answer_test()
