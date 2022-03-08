__all__ = ['User'] # 只是针对 from 包 import * 起作用

version =1.0

class User:
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def login(self,username,password):
        if self.username == username and self.password == password:
            print('登陆成功')
        else:
            print('登陆失败')
    def show(self):
        print('输入的用户名是:{}, 密码是:{}'.format(self.username,self.password))

    def __str__(self):
        return '输入的用户名是:{}, 密码是:{}'.format(self.username,self.password)

    def publish_article(self,article):
        # article传递的是对象
        print('{}发布了{}剧作'.format(self.username,article.name))

# 控制本包执行的时候调用, 其他不会被调用
if __name__ == '__main__':
    print('--------user----------')