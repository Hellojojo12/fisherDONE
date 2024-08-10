from flask import request
from wtforms import Form
from wtforms.validators import DataRequired as WTFDataRrequired


class DataRequired(WTFDataRrequired):
    """
        重写默认的WTF DataRequired，实现自定义message
        DataRequired是一个比较特殊的验证器，当这个异常触发后，
        后续的验证（指的是同一个validators中的验证器将不会触发。
        但是其他验证器，比如Length就不会中断验证链条。
    """

    def __call__(self, form, field):
        if self.message is None:
            field_text = field.label.text
            self.message = field_text + '不能为空，请填写' + field_text
        super().__call__(form, field)
