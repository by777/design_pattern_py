# -*- coding: utf-8 -*-
# @Author  : Xu Bai
# @Time    : 2022/6/2 下午4:13
# @Desc    :
from abc import ABCMeta, abstractmethod


# 抽象产品
class PhoneShell(metaclass=ABCMeta):
    @abstractmethod
    def show_shell(self):
        pass


class CPU(metaclass=ABCMeta):
    @abstractmethod
    def show_cpu(self):
        pass


class OS(metaclass=ABCMeta):
    @abstractmethod
    def show_os(self):
        pass


# 抽象工厂
class PhoneFactory(metaclass=ABCMeta):
    @abstractmethod
    def make_shell(self):
        pass

    @abstractmethod
    def make_cpu(self):
        pass

    @abstractmethod
    def make_os(self):
        pass


# 具体产品
class SmallShell(PhoneShell):
    def show_shell(self):
        print('普通小手机壳')


class BigShell(PhoneShell):
    def show_shell(self):
        print('普通大手机壳')


class AppleShell(PhoneShell):
    def show_shell(self):
        print('普通Apple手机壳')


class SnapDragonCpu(CPU):
    def __init__(self, is_gaopei=False):
        self.is_gaopei = is_gaopei

    def show_cpu(self):
        print('小龙CPU')


class MediaTekCpu(CPU):
    def show_cpu(self):
        print('连发科CPU')


class AppleCpu(CPU):
    def show_cpu(self):
        print('A14 CPU')


class Android(OS):
    def show_os(self):
        print('安卓操作系统')


class Ios(OS):
    def show_os(self):
        print('Ios操作系统')


# 具体工厂
class MiFactory(PhoneFactory):
    def make_shell(self):
        return BigShell()

    def make_cpu(self):
        return SnapDragonCpu()

    def make_os(self):
        return Android()


class HuaweiFactory(PhoneFactory):
    def make_shell(self):
        return SmallShell()

    def make_cpu(self):
        return MediaTekCpu()

    def make_os(self):
        return Android()


class IPhoneFactory(PhoneFactory):
    def make_shell(self):
        return SmallShell()

    def make_cpu(self):
        return AppleCpu()

    def make_os(self):
        return Ios()


# 客户端
class Phone:
    def __init__(self, cpu, os, shell):
        self.cpu, self.os, self.shell = cpu, os, shell

    def show_info(self):
        print('手机信息：')
        self.cpu.show_cpu()
        self.os.show_os()
        self.shell.show_shell()


def make_phone(factory):
    cpu = factory.make_cpu()
    os = factory.make_os()
    shell = factory.make_shell()
    return Phone(cpu, os, shell)


p1 = make_phone(MiFactory())
p1.show_info()
