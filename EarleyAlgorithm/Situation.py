class Situation:
    out = str  # из чего
    to = str  # во что
    i = int  # позиция в слове w
    point = int  # позиция в to, перед которой стоит точка

    def __init__(self, str_out, str_to, int_i, int_point):
        self.out = str_out
        self.to = str_to
        self.ind = int_i
        self.point = int_point
