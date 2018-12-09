class Rule:
    out = str  # левая часть правила (из чего выводится)
    to = str  # правая часть правила (что выводится)

    def __init__(self, str_out, str_to):
        self.out = str_out
        self.to = str_to
