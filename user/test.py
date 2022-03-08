# 实现用户发表文章


# 创建用户对象
from user.module import User
user = User('admin','123123')
user.show()
# 发表文章, 创建文章对象
from article.module import Article
article = Article('三国演义','罗贯中')
user.publish_article(article)

# 调用calculate求和
from calculate import add
lists = [1,2,3]
result = add(*lists)
print(result)

MAX = 100
