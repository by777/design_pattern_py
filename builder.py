# -*- coding: utf-8 -*-
# @Author  : Xu Bai
# @Time    : 2022/6/5 下午1:59
# @Desc    :
print('''
-------------------------------------------------------------------------------- 
建造者模式，将一个复杂对象的构建与表示相分离，使得同样的构建过程可以创建不同的表示
和抽象工厂模式比较相似，也用来创建一个复杂对象。
主要区别是建造者模式着重一步一步构造一个复杂对象，而抽象工厂模式着重于对个系列的产品对象。

角色：
    抽象建造者-Builder
    具体建造者-Concrete Builder
    指挥者-Director
    产品-Product
--------------------------------------------------------------------------------    
''')
from abc import abstractmethod, ABCMeta


class Player:
    def __init__(self, face=None, body=None, arm=None, leg=None):
        self.face = face
        self.body = body
        self.arm = arm
        self.leg = leg

    def __str__(self):
        return f'{self.face}, {self.body}, {self.arm}, {self.leg}'


class PlayerBuilder(metaclass=ABCMeta):
    @abstractmethod
    def build_face(self):
        pass

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def build_arm(self):
        pass

    @abstractmethod
    def build_leg(self):
        pass


class SexyGirlBuilder(PlayerBuilder):

    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = "漂亮脸蛋"

    def build_body(self):
        self.player.body = "苗条"

    def build_arm(self):
        self.player.arm = "细长胳膊"

    def build_leg(self):
        self.player.leg = "大长腿"


class Monster(PlayerBuilder):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = "怪兽脸"

    def build_body(self):
        self.player.body = "怪兽身材"

    def build_arm(self):
        self.player.arm = "毛胳膊"

    def build_leg(self):
        self.player.leg = "毛腿"


class PlayerDirector:
    # 控制组装顺序
    def builder_player(self, builder):
        builder.build_body()
        builder.build_face()
        builder.build_arm()
        builder.build_leg()
        return builder.player


# 客户端
builder = SexyGirlBuilder()
builder1 = Monster()
director = PlayerDirector()
p = director.builder_player(builder)
p1 = director.builder_player(builder1)
print(p, "\n", p1)
