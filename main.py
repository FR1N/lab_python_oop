from rectangle import Rectangle
from circle import Circle
from square import Square

if __name__ == "__main__":
    rect = Rectangle(3, 2, 'синий')
    print(rect.__repr__())

    crl = Circle(5, 'зеленый')
    print(crl.__repr__())

    sqrt = Square(5, 'красный')
    print(sqrt.__repr__())
