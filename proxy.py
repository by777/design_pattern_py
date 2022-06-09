# -*- coding: utf-8 -*-
# @Author  : Xu Bai
# @Time    : 2022/6/7 下午8:12
# @Desc    :
from abc import ABCMeta, abstractmethod

print("""
角色：
    抽象实体（Subject）
    实体（RealSubject）
    代理（Proxy）
优点：
    远程代理：可以隐藏对象位于远程空间地址的事实
    虚代理：可以进行优化，例如根据要求创建对象
    保护代理：允许在访问一个对象时有一些附加的内务处理
    --------------------------------------------------
""")


class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class RealSubject(Subject):
    def __init__(self, filename):
        self.filename = filename
        f = open(filename, 'r', encoding='utf-8')
        print('读取文件内容')
        self.content = f.read()
        # print(self.content)
        f.close()

    def get_content(self):
        return self.content

    def set_content(self, content):
        f = open(self.filename, 'w', encoding='utf-8')
        f.write(content)
        f.close()


# 虚代理
class VirtualProxy(Subject):
    def __init__(self, filename):
        self.filename = filename
        self.subj = None

    def get_content(self):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.get_content()

    def set_content(self, content):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.set_content(content)


# subj = RealSubject('test.txt')
# 下面一行不会提前执行open函数
subj1 = VirtualProxy('test.txt')
# 调用时才会执行open
print(subj1.get_content())


# 保护代理
class ProtectProxy(Subject):
    def __init__(self, filename):
        self.subj = RealSubject(filename)

    def get_content(self):
        return self.subj.get_content()

    def set_content(self, content):
        raise PermissionError('无写入权限！')


subj = ProtectProxy('test.txt')
print(subj.get_content())
subj.set_content('能写入成功吗？')
