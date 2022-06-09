# -*- coding: utf-8 -*-
# @Author  : Xu Bai
# @Time    : 2022/6/6 下午6:13
# @Desc    :
from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Payment):
    def pay(self, money):
        print(f'支付宝支付{money}元')


class WechatPay(Payment):
    def pay(self, money):
        print(f'微信支付{money}元')


class BankPay:
    def cost(self, money):
        print(f'银联支付{money}元')


class ApplePay:
    def cost(self, money):
        print(f'Apple支付{money}元')


# p = Alipay(), P = BankPay()
# p.pay(100)
# 本来想BankPay，但是BankPay没有pay接口

# 类适配器：使用多继承
class NewBankPay(Payment, BankPay):
    """
    继承（实现）Payment的目的是接口统一,
    继承BankPay的目的是复用BankPay的代码，没有必要重新写
    """

    def pay(self, money):
        self.cost(money)


p = Alipay()
p.pay(100)
# 本来想BankPay，但是BankPay没有pay接口
p = NewBankPay()
p.pay(1000)


# 对象适配器：使用组合
class PaymentAdapter(Payment):
    def __init__(self, payment):
        self.payment = payment

    def pay(self, money):
        self.payment.cost(money)


p = PaymentAdapter(ApplePay())
p.pay(1)
p = PaymentAdapter(BankPay())
p.pay(11)


# 组合：一个类里放入另一个类的对象
class A:
    pass


class B:
    def __init__(self):
        self.a = A()
