from rectangle import Rectangle, FigureColor


class Square(Rectangle):
    name = "Квадрат"

    def __init__(self, width, color):
        self.color = FigureColor
        self.color.color = color
        self.width = width

    def area(self):
        return self.width ** 2

    def __repr__(self):
        return "Тип фигуры: {a}, цвет: {b}, сторона: {c}, площадь: {d}".format(a=self.name, b=self.color.color,
                                                                               c=self.width,
                                                                               d=self.area())



