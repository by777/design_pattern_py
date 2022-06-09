# -*- coding: utf-8 -*-
# @Author  : Xu Bai
# @Time    : 2022/6/6 下午7:02
# @Desc    :
"""

# 非常不容易扩展

class Shape:
    pass


class Line(Shape):
    ...


class Rectangle(Shape):
    ...


class Circle(Shape):
    ...


class RedLine(Line):
    pass


class GreenLine(Line):
    ...


class BlueLine(Line):
    pass
"""
from abc import abstractmethod, ABCMeta


class Shape(metaclass=ABCMeta):

    def __init__(self, color):
        self.color = color

    @abstractmethod
    def draw(self):
        ...


class Color(metaclass=ABCMeta):
    @abstractmethod
    def paint(self, shape):
        ...


class Rectangle(Shape):
    name = '长方形'

    def draw(self):
        self.color.paint(self)


class Circle(Shape):
    name = '圆形'

    def draw(self):
        self.color.paint(self)


class Red(Color):
    def paint(self, shape):
        print(f'红色的{shape.name}')


class Green(Color):
    def paint(self, shape):
        print(f'绿色的{shape.name}')


# 客户端
Rectangle(Red()).draw()
Circle(Green()).draw()


class Line(Shape):
    name = '直线'

    def draw(self):
        self.color.paint(self)


Line(Red()).draw()
