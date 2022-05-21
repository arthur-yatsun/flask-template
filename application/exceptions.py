class BaseException(Exception):
    """Base exception class"""
    def __init__(self, message):
        super().__init__(message)


class FieldNotFound(BaseException):
    """Field not found exception"""


class BaseSessionError(BaseException):
    """Base session error"""
