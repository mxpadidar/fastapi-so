from core.errors import BaseError


class UnAuthenticatedError(BaseError):
    def __init__(self, message: str = "Invalid credentials") -> None:
        super().__init__(message, 401)
