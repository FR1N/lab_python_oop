from abc import ABC, abstractmethod


class GeomFigure(ABC):
    @abstractmethod
    def area(self):
        print("Площадь фигуры")





