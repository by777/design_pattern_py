# -*- coding: utf-8 -*-
# @Author  : Xu Bai
# @Time    : 2022/5/27 下午3:30
# @Desc    :

##################################################################
# 接口：若干抽象方法的集合                                          #
# 作用：1.限制实现接口的类必须按照接口给定的调用方式实现这些方法；       #
#      2.对高层模块隐藏了类的内部实现                               #
#################################################################

# 方式1，实例化不报错，调用时抛出异常
# class Payment:
#     def pay(self, money):
#         raise NotImplemented

# 方式2，更常用
from abc import ABCMeta, abstractmethod


# abc = abstract class
class Payment(metaclass=ABCMeta):
    # 抽象方法，约束子类必须要实现该方法
    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Payment):
    # 继承抽象类，必须要实现抽象方法，否则不能实例化
    def pay(self, money):
        print(f'支付宝支付{money}元。')


class WechatPay(Payment):
    def pay(self, money):
        print(f'微信支付{money}元。')


p = Alipay()
p.pay(100)


# def finish_pay(p: Alipay, money):
#     p.pay(100)
class User:
    def show_name(self):
        ...


class VipUser(User):
    def show_name(self):
        ...


u = User()
res = u.show_name()

'''
这种接口设计方式不合理，不应该所有的子类都实现所有方法，解决办法是拆开
class Animal(metaclass=ABCMeta):

    @abstractmethod
    def walk(self):
        ...

    @abstractmethod
    def swim(self):
        ...

    @abstractmethod
    def fly(self):
        ...
'''


class LandAnimal(metaclass=ABCMeta):
    @abstractmethod
    def walk(self):
        ...


class WaterAnimal(metaclass=ABCMeta):
    @abstractmethod
    def swim(self):
        ...


class SkyAnimal(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        ...


class Tiger(LandAnimal):
    def walk(self):
        print("老虎只走路")


class Frog(LandAnimal, WaterAnimal):
    # 青蛙利用多继承实现两个方法
    def walk(self):
        print("青蛙走路")

    def swim(self):
        print("青蛙游泳")
