class Rule:
    input = str  # левая часть правила (из чего выводится)
    output = str  # правая часть правила (что выводится)

    def __init__(self, str_input, str_output):
        self.input = str_input
        self.output = str_output
