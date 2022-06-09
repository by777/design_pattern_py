# -*- coding: utf-8 -*-
# @Author  : Xu Bai
# @Time    : 2022/5/30 上午10:41
# @Desc    :

# ===================
# 简单工厂模式：不直接向客户端暴露创建对象的实现细节，而是通过一个工厂来负责创建产品类的实例

from abc import ABCMeta, abstractmethod


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


class PaymentFactory:
    # 应对于处理多参数等情况时隐藏信息
    def create_payment(self, method):
        if method.lower() == 'alipay':
            return Alipay()
        elif method.lower() == 'wechat':
            return WechatPay()
        elif method.lower() == 'huabai':
            return Alipay(use_huabai=True)
        else:
            raise TypeError(f"No such payment named {method}")


# client
pf = PaymentFactory()
p = pf.create_payment('huabai')
p.pay(100)
