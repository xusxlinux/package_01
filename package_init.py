"""
__init__.py文件
当导入包的时候, 默认调用 __init__.py这个文件
作用:
  1. 当导入包的时候, 把一些初始化的变量, 函数放到  __init__.py 这个文件中
  2. 此文件中的函数,变量的访问, 只需要通过包名, 函数...
  3. 在__init__.py中结合  __all__ = [通过* 可以访问的模块]
"""

from user.module import User
import user
user.create_app()

"""
    :from 模块 import *
      *号表示使用模块内的所有内容如果没有定义__all__ = ['',''] 所有的都可以访问
      但是添加上__all__ = ['',''] 只有列表中的可以访问
    
    
    :from 包名 import *
      表示该包中内容(模块)是不能访问, 就需要在__init__.py文件中定义__all__ = ['module', 'module1', 'module2']
"""
from user import *
user = module.User('admin','123')   # __init__.py 中添加 __all__ = ['module']
print(user)

result = test.MAX
print(result)
