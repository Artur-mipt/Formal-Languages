class Situation:
    input = str  # из чего
    output = str  # во что
    ind = int  # позиция в слове w
    point = int  # позиция в to, перед которой стоит точка

    def __init__(self, str_input, str_output, int_i, int_point):
        self.input = str_input
        self.output = str_output
        self.ind = int_i
        self.point = int_point
