"""
架构设计不当, 会出现项目中, 你引用我, 我引用你的情况

循环导入:
A: 模块
  def test():
    f()
B: 模块
  def f():
    test()

如何避免循环导入:
  大型python项目中, 需要很大py文件,由于架构不当, 可能会出现模块之间的相互导入

  解决:
  1. 重写架构
  2. 把要使用的引用 放到代 需要使用代码附近
"""
from daem_02_循环导入 import func


def task1():
    print('-----task1-----')

def task2():
    print('-----task2-----')
    func()

# 加上main的时候 import调用将不会被执行
if __name__ == '__main__':
    task1()
    task2()