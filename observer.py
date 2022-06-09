# -*- coding: utf-8 -*-
# @Author  : Xu Bai
# @Time    : 2022/6/8 下午3:42
# @Desc    :
from abc import ABCMeta, abstractmethod

print("""
内容：
    定义对象间的一种一对多的依赖关系，当一个对象的状态发生变化时，所有依赖它的对象都得到通知并自动更新。
    观察者模式又称为发布-订阅模式
角色：
    抽象主题（Subject）
    具体主题（ConcreteSubject）- 发布者
    抽象观察者（Observer）
    具体观察者（ConcreteObserver）- 订阅者
    -------------------------------------------------------------------------------------
""")


# 抽象订阅者
class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, notice):  # notice应该是一个Notice类的对象，或者子类
        pass


# 抽象发布者 - Notice
class Notice:
    def __init__(self):
        # 存储这个发布者所有的订阅对象
        self.observers = []

    # 订阅
    def attach(self, obs):
        self.observers.append(obs)

    # 解除绑定
    def detach(self, obs):
        self.observers.remove(obs)

    # 推送
    def notify(self):
        for obs in self.observers:
            obs.update(self)


# 具体的发布者 - 员工通知
class StaffNotice(Notice):
    def __init__(self, company_info):
        super().__init__()  # 调用父类的init函数，生成一个observers属性
        self.__company_info = company_info  # 定义自己的私有成员

    @property  # 属性装饰器
    def company_info(self):
        return self.__company_info

    @company_info.setter
    def company_info(self, info):
        self.__company_info = info
        self.notify()


# 具体的订阅者
class Staff(Observer):
    def __init__(self):
        # 也要维护一个自己的company_info
        self.company_info = None

    def update(self, notice):
        self.company_info = notice.company_info


notice = StaffNotice('初始公司信息')
s1 = Staff()
s2 = Staff()
notice.attach(s1)
notice.attach(s2)
print(s1.company_info)
notice.company_info = '加薪'
print(s1.company_info)
