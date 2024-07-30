from app.libs.helper import get_isbn


class BookViewModel:
    def __init__(self, data):
        self.title = data['bookName']
        self.author = '、'.join(data['author'])
        self.binding = data['binding']
        self.publisher = data['press']
        self.image = data['image']
        self.price = '￥{:.2f}'.format(data.get('price', 0) / 100)
        self.isbn = get_isbn(data)
        self.pubdate = data['pressDate']
        self.summary = data['bookDesc']
        self.pages = data['pages']

    @property
    def intro(self):
        intros = filter(lambda x: True if x else False,
                        [self.author, self.publisher, self.price])
        return ' / '.join(intros)


class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = None

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.books = [BookViewModel(book) for book in yushu_book.books]
        self.keyword = keyword

