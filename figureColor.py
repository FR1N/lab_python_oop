class FigureColor:

    def __init__(self, color):
        self.color = color

    @property
    def color(self):
        return self.color

    @color.setter
    def color(self, clr):
        self.color = clr