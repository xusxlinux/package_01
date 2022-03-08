# from daem_01_循环导入 import task1


def func():
    print('-----循环导入2里面func----->1')
    # 把要使用的 放到代码中
    from daem_01_循环导入 import task1
    task1()
    print('-----循环导入2里面func----->2')