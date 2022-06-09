# -*- coding: utf-8 -*-
# @Author  : Xu Bai
# @Time    : 2022/6/8 下午5:04
# @Desc    :
from abc import ABCMeta, abstractmethod

from time import sleep


# 实现了一个模板方法，但留了很多原子操作（钩子操作）
class Window(metaclass=ABCMeta):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def repaint(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    # 模板方法，定义了框架，细节没有定义
    def run(self):
        self.start()
        while True:
            try:
                self.repaint()
                sleep(1)
            except KeyboardInterrupt:
                break
        self.stop()


class MyWindow(Window):
    def __init__(self, msg):
        self.msg = msg

    def start(self):
        print('开始运行窗口')

    def repaint(self):
        print(self.msg)

    def stop(self):
        print('窗口结束运行')


MyWindow('Hello').run()
