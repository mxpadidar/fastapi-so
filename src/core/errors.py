class BaseError(Exception):
    def __init__(self, message: str, code: int) -> None:
        super().__init__(message)
        self.message = message
        self.code = code


class NotFoundError(BaseError):
    def __init__(self, message: str = "Resource not found") -> None:
        super().__init__(message, 404)


class ConflictError(BaseError):
    def __init__(self, message: str = "Resource already exists") -> None:
        super().__init__(message, 409)


class ValidationError(BaseError):
    def __init__(self, message: str = "Validation error") -> None:
        super().__init__(message, 422)
