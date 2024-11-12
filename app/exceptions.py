from fastapi import HTTPException


class AppException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


# ___Users___#


class UserAlreadyExistsException(AppException):
    status_code = 409
    detail = "Пользователь уже существует"


class UserLoginException(AppException):
    status_code = 401
    detail = "Неверный email или пароль"


# __________#


class PointNotFoundException(AppException):
    status_code = 404
    detail = "Точка не найдена"


class NotYourPointException(AppException):
    status_code = 403
    detail = "Это не ваша точка"


class PermissionDeniedException(AppException):
    status_code = 403
    detail = "Недостаточно прав"


class SMTPException(AppException):
    status_code = 500
    detail = "Ошибка при отправке сообщения"
