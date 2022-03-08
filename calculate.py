"""

当不想星号渠道所有的值可以使用一下的方式:

"""
# __all__ = ['add','number']
number = 100

def add(*args):
    if len(args) > 1:
        sum = 0
        for i in args:
            sum += i
        return sum
    else:
        print('至少传入两个参数')

def subtraction(*args):
    if len(args) > 1:
        sum = 0
        for i in args:
            sum -= i
        return sum
    else:
        print('至少传入两个参数')

class Calculate:
    def __init__(self,number):
        self.number = number

    def test(self):
        print('正在使用calculate')

    @classmethod
    def test1(cls):
        print('正在使用calculate类方法')

# 这个模块被调用的时候, 会把 *号中调用的所有内容都加载到内存
def test1():
    print('test1,在calculate中被调用')


# 在本模块打印出来的还是__main__, 但是其他的模块调用就是: calculate
print('__name__', __name__)
#test1()
# 涉及到函数的调用都会去执行, 但是把调用放到if中, 运行daem_02_模块.py 不会出现  "test1,在calculate中被调用"这句话
if __name__ == '__main__':
    # 在模块的类中要打印本身的__name__  输出 __main__  所以在本模块中,叫做__main__ 出了本模块名称就变了
    print(__name__)
    test1()
