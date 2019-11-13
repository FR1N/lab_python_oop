from geomFigure import GeomFigure
from figureColor import FigureColor
import math


class Circle(GeomFigure):
    name = "Круг"

    def __init__(self, radius, color):
        self.color = FigureColor
        self.color.color = color
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def __repr__(self):
        return "Тип фигуры: {a}, цвет: {b}, радиус: {c}, площадь: {d}".format(a=self.name, b=self.color.color,
                                                                              c=self.radius,
                                                                              d=self.area())
