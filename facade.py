# -*- coding: utf-8 -*-
# @Author  : Xu Bai
# @Time    : 2022/6/7 下午7:58
# @Desc    :
print("""
    为子系统中的一组接口提供一个一致的界面，外观模式定义了一个高层接口，
    这一接口使得这一子系统更加容易使用。
    --------------------------------------------------------
""")


class CPU:
    def run(self):
        print('CPU running...')

    def stop(self):
        print('CPU stopped')


class Disk:
    def run(self):
        print('Disk running...')

    def stop(self):
        print('Disk stopped')


class Memory:
    def run(self):
        print('Memory running...')

    def stop(self):
        print('Memory stopped')


# Facade外观
class Computer:
    # 需要3个子系统
    def __init__(self):
        self.cpu = CPU()
        self.disk = Disk()
        self.memory = Memory()

    def run(self):
        self.cpu.run()
        self.disk.run()
        self.memory.run()

    def stop(self):
        self.cpu.stop()
        self.disk.stop()
        self.memory.stop()


pc = Computer()
# 目的通过一个统一的接口进行调用
pc.run()
pc.stop()
