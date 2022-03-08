
"""

from 包 import 模块
from 包.模块 import 类 | 函数 | 变量
from 包 import *
"""

"""方式一"""
from user import module
u = module.User('吴承恩','123456')
u.show()

from article import module
a = module.Article('西游记','吴承恩')
a.show()

"""方式二"""
from user.module import User
u = User('施耐庵','123456')
u.show()

from article.module import Article
a = Article('水浒传','施耐庵')
a.show()





