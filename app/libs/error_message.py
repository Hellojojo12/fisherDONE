class FormException:
    pass


'''
AI生成的代码
'''


class BaseException(Exception):
    def __init__(self, message=None, http_code=400, extra_data=None):
        """
        :param message: 错误消息，可以为空，默认消息会覆盖它
        :param http_code: HTTP 状态码，默认为 400
        :param extra_data: 额外的错误数据，可以用于提供更多上下文信息
        """
        self.message = message or "An error occurred."
        self.http_code = http_code
        self.extra_data = extra_data or {}

    def get_args(self):
        """
        返回一个包含错误信息的字典
        """
        return {
            "message": {
                "error": self.message,
                "data": self.extra_data
            },
            "http_code": self.http_code
        }

    def __str__(self):
        """
        返回异常的字符串表示形式
        """
        return f"{self.http_code} - {self.message}"


class UnknownException(BaseException):
    def __init__(self, extra_data=None):
        """
        初始化时自动设置 HTTP 状态码为 500，并使用默认错误消息
        """
        super().__init__(message="服务器内部错误", http_code=500, extra_data=extra_data)
