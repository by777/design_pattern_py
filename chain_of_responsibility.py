# -*- coding: utf-8 -*-
# @Author  : Xu Bai
# @Time    : 2022/6/8 下午2:46
# @Desc    :
from abc import ABCMeta, abstractmethod

print("""
责任链模式：
内容：
    使多个对象都有机会处理请求，从而避免请求的发送者和接收者之间的耦合关系。
    将这些对象连成一条链，并沿着这条链传递请求，直到有一个对象处理它为止
角色：
    抽象处理者（Handler）
    具体处理者（ConcreteHandler）
    客户端（Client）
    ------------------------------------------------------------
""")


# 有几个不同的请求的处理者，这些处理者应该是对外表现一致的
class Handler(metaclass=ABCMeta):
    @abstractmethod
    def handle_leave(self, day):
        pass


# 总经理可以处理者10天以内的请假
class GeneralManager(Handler):
    def handle_leave(self, day):
        if day <= 10:
            print(f'总经理准假{day}天')
        else:
            print('总经理说：你还是辞职吧')


# 部门经理
class DepartmentManager(Handler):
    def __init__(self):
        self.next = GeneralManager()

    def handle_leave(self, day):
        if day <= 5:
            print(f'部门经理准假{day}天')
        else:
            print('部门经理权限不足，交给下一位>>>')
            self.next.handle_leave(day)


# 项目主管，
class ProjectDirector(Handler):
    def __init__(self):
        self.next = DepartmentManager()

    def handle_leave(self, day):
        if day <= 3:
            print(f'科目主管准假{day}天')
        else:
            print('项目主管权限不足，交给上级处理>>>')
            self.next.handle_leave(day)


day = 1
h = ProjectDirector()
h.handle_leave(day)
