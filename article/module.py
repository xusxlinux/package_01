class Article:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def show(self):
        print('发表文章的名字:{}, 作者是:{}'.format(self.name, self.author))

    def __str__(self):
        return '发表文章的名字:{}, 作者是:{}'.format(self.name, self.author)


class Tag:
    def __init__(self, name):
        self.name = name
