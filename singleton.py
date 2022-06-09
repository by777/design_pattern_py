# -*- coding: utf-8 -*-
# @Author  : Xu Bai
# @Time    : 2022/6/5 下午2:24
# @Desc    :

# 基类
class Singleton:
    # new在init之前调用，用来分配空间
    def __new__(cls, *args, **kwargs):
        """
        用一个类属性来表示这个类的实例
        如果类有这个属性了，就说明这个类有实例了，就直接把这个实例返回过去，
        若是没有，再创建
        """
        if not hasattr(cls, "_instance"):
            # cls是这个类
            # 这个类没有实例,调用父类Object的new方法去创建这个实例
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class MyClass(Singleton):
    def __init__(self, a):
        self.a = a


a = MyClass(10)
print("""
会发生：
    会创建一个MyClass这个对象，在调用init之前，对调用MyClass的new，
    其实也就是Singleton的new。 
    会发现没有_instance这个类属性，
    于是，去调用父类（Object）的super方法（new），把class传递进去
""")
b = MyClass(20)
print(a.a)
