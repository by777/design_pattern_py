# -*- coding: utf-8 -*-
# @Author  : Xu Bai
# @Time    : 2022/6/8 下午4:35
# @Desc    :
from abc import ABCMeta, abstractmethod


class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, data):
        pass


class FastStrategy(Strategy):
    def execute(self, data):
        print(f'用较快的速度处理{data}')


class SlowStrategy(Strategy):
    def execute(self, data):
        print(f'用较慢的速度处理{data}')


class Context:
    def __init__(self, strategy, data):
        self.data = data
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def do_strategy(self):
        self.strategy.execute(data=self.data)


# Client
data = '从上海到北京'
s = FastStrategy()
context = Context(s, data)
context.do_strategy()
context.set_strategy(SlowStrategy())
context.do_strategy()
