# 0731
**hasattr(object, name)**
-object: 要检查属性的对象。
-name: 一个字符串，表示你想检查的属性名称。

**json.dumps（）**
-Python 对象序列化为 JSON 格式的字符串

**json.loads（）**
-用于将 JSON 格式的字符串解析为 Python 对象

**Cache**
-缓存
-案例设置为内存缓存，这个函数运行过一次后，会将运行结果保存在服务器中，再次访问会直接返回
-内存中的结果，有时效性
-from flask_caching import Cache
-app.config['CACHE_TYPE'] = 'SimpleCache'  # 指定缓存类型为简单内存缓存
-cache = Cache(app)  # 初始化缓存
--
-@app.route('/')
@cache.cached(timeout=60)  # 缓存此视图的结果60秒
-def index():
    return "Hello, world!"

**WSGI** 
-是一种标准化的接口，定义了 Python Web 服务器和应用之间的通信方式。

**token**
-from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
-通过序列化的方式进行加密和解密
-要在系统中配置key

**数据库查询方式**
`-gift = Gift.query.get(current_gift_id)
-Drift.query.filter(Drift.pending == PendingStatus.success, Gift.uid == self.id).count()`
-其实就是两种 get()和filter()

