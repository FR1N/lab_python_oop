from geomFigure import GeomFigure
from figureColor import FigureColor


class Rectangle(GeomFigure):
    name = "Прямоугольник"

    def __init__(self, width, height, color):
        self.color = FigureColor
        self.color.color = color
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return "Тип фигуры: {a}, цвет: {b}, ширина: {c}, высота: {d}, площадь: {e}".format(a=self.name,
                                                                                           b=self.color.color,
                                                                                           c=self.width, d=self.height,
                                                                                           e=self.area())



