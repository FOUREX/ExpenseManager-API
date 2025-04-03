from fastapi import status

from src.domain.common.exceptions.base import BaseAppError


class AppError(BaseAppError):
    pass


class ServerError(AppError):
    code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = "Unexpected error"
