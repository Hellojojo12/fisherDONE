from app.libs.http import Http



class YuShuBook:
    per_page = 15
    isbn_url = 'http://data.isbn.work/openApi/getlnfoBylsbn?isbn={isbn}&appKey={appkey)'
    app_key = 'ae1718d4587744b0b79f940fbef69e77'
    # isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.total = 0
        self.books = []
    # books里面是从接口查询过来的一个个字典，每个字典是一本书籍的信息

    # @cache.memoize(timeout=60)
    def search_by_isbn(self, isbn):
        url = self.isbn_url.format(isbn=isbn, appkey=self.app_key)
        result = Http.get(url)
        self.__fill_single(result)

    def search_by_keyword(self, keyword, page):
        page = int(page)
        url = self.keyword_url.format(keyword, self.per_page, self.per_page * (page - 1))
        result = Http.get(url)
        self.__fill_collection(result)

    @property
    def first(self):
        return self.books[0] if self.total >= 1 else None

    def __fill_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection(self, data):
        self.total = data['total']
        self.books = data['books']

