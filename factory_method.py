# -*- coding: utf-8 -*-
# @Author  : Xu Bai
# @Time    : 2022/5/30 上午10:59
# @Desc    :
from abc import ABCMeta, abstractmethod

print("""
====================================================================
内容：定义一个用于创建对象的接口（工厂接口），让子类决定去实例化哪一个产品类
角色：

+ 抽象工厂角色（Creator）
+ 具体工厂角色（Concrete Creator）
+ 抽象产品角色（Product）
+ 具体产品角色（Concrete Product)
====================================================================
""")


# 抽象产品
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        ...


class Alipay(Payment):
    def __init__(self, use_huabai=False):
        self.use_huabai = use_huabai

    def pay(self, money, use_huabai=False):
        if self.use_huabai:
            print(f"花呗支付{money}元")
        else:
            print(f"支付宝余额支付{money}元")


class WechatPay(Payment):

    def pay(self, money):
        print(f"微信支付{money}元")


class BankPay(Payment):
    def pay(self, money):
        print(f"银行支付{money}元")


# 约束工厂
class PaymentFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_payment(self):
        ...


class AlipayFactory(PaymentFactory):
    def create_payment(self):
        return Alipay()


class WechatPayFactory(PaymentFactory):
    def create_payment(self):
        return WechatPay()


class HuabaiFactory(PaymentFactory):
    def create_payment(self):
        return Alipay(use_huabai=True)


class BankFactory(PaymentFactory):
    def create_payment(self):
        return BankPay()


pf = HuabaiFactory()
p = pf.create_payment()
p.pay(100)

# pf = BankFactory()
# p = pf.create_payment()
# p.pay(100)
BankFactory().create_payment().pay(100)
