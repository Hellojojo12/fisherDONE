# -*- coding: utf-8 -*-
__author__ = 'JOJO'

from datetime import timedelta

# SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:7insummer@139.196.96.50:3307/fisher'
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:password@localhost/fisher'
SECRET_KEY = '\x88D\xf09\x91\x07\x98\x89\x87\x96\xa0A\xc68\xf9\xecJ:U\x17\xc5V\xbe\x8b\xef\xd7\xd8\xd3\xe6\x98*4'

# Email 配置
MAIL_SERVER = 'smtp.exmail.qq.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TSL = False
MAIL_USERNAME = 'hello@yushu.im'
MAIL_PASSWORD = 'Bmwzy1314520'
MAIL_SUBJECT_PREFIX = '[鱼书]'
MAIL_SENDER = '鱼书 <hello@yushu.im>'

# 开启数据库查询性能测试
SQLALCHEMY_RECORD_QUERIES = True

# 性能测试的阀值
DATABASE_QUERY_TIMEOUT = 0.5

SQLALCHEMY_TRACK_MODIFICATIONS = True

WTF_CSRF_CHECK_DEFAULT = False

SQLALCHEMY_ECHO = True

REMEMBER_COOKIE_DURATION = timedelta(days=30)

PROXY_API = 'http://ip.yushu.im/get'

# PERMANENT_SESSION_LIFETIME = 3600
