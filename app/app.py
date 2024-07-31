from datetime import datetime, date
# from flask.json import JSONEncoder as _JSONEncoder
# flask2.3之后的版本舍弃了JSONEncoder
from flask.json.provider import JSONProvider as _JSONEncoder
from flask import Flask as _Flask


# hasattr(object, name)
# object: 要检查属性的对象。
# name: 一个字符串，表示你想检查的属性名称。
class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            print(o)
            return dict(o)
        if isinstance(o, datetime):
            return o.strftime('%Y-%m-%dT%H:%M:%SZ')
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        return super().default(o)


class Flask(_Flask):
    # json_encoder = JSONEncoder
    json_provider_class = JSONEncoder


