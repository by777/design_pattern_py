# -*- coding: utf-8 -*-
# @Author  : Xu Bai
# @Time    : 2022/6/6 下午7:40
# @Desc    :
from abc import ABCMeta, abstractmethod

print("""
使用场景：
    表示对象的“部分-整体”层次结构（特别结构是递归的）
    希望用户忽略组合对象与单个对象的不同，用户统一的使用组合结构的所有对象
优点：
    定义了包括基本对象和组合对象的层次结构
    简化客户端代码，即客户端可以一致的使用组合对象和单个对象
    更容易增加新类型的组件
------------------------------------------------------------------
""")


class Graphic(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass


# 简单对象
class Point(Graphic):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'点({self.x}, {self.y})'

    def draw(self):
        print(str(self))


class Line(Graphic):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return '线段[%s, %s]' % (self.p1, self.p2)

    def draw(self):
        print(str(self))


# 复杂对象
class Picture:
    def __init__(self, iterable):
        self.children = []
        for g in iterable:
            self.add(g)

    def add(self, graphic):
        self.children.append(graphic)

    def draw(self):
        print('+-+-+-复合图形+-+-+-')
        for g in self.children:
            g.draw()
        print('------复合图形------')


l = Line(Point(1, 1, ), Point(2, 2))
print(l)
p1 = Point(2, 3)
l1 = Line(Point(3, 4), Point(6, 7))
l2 = Line(Point(1, 5), Point(2, 8))
pic1 = Picture([p1, l1, l2])
pic1.draw()
pic2 = Picture([pic1, pic1, l1])
pic2.draw()
