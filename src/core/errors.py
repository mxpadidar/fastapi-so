class BaseError(Exception):
    def __init__(self, message: str, http_status_code: int) -> None:
        super().__init__(message)
        self.message = message
        self.status_code = http_status_code


class NotFoundError(BaseError):
    def __init__(self, message: str = "Resource not found") -> None:
        super().__init__(message, 404)


class ConflictError(BaseError):
    def __init__(self, message: str = "Resource already exists") -> None:
        super().__init__(message, 409)


class UnAuthenticatedError(BaseError):
    def __init__(self, message: str = "Invalid credentials") -> None:
        super().__init__(message, 401)


class ValidationError(BaseError):
    def __init__(self, message: str = "Validation error") -> None:
        super().__init__(message, 422)
