"""
Custom application exceptions
"""
from typing import Optional

class AppException(Exception):
    """Base application exception"""
    def __init__(self, detail: str, status_code: int = 400, error_code: Optional[str] = None):
        self.detail = detail
        self.status_code = status_code
        self.error_code = error_code
        super().__init__(detail)

class ValidationError(AppException):
    """Validation error exception"""
    def __init__(self, detail: str):
        super().__init__(detail, 422, "VALIDATION_ERROR")

class NotFoundError(AppException):
    """Not found error exception"""
    def __init__(self, detail: str = "Resource not found"):
        super().__init__(detail, 404, "NOT_FOUND")

class UnauthorizedError(AppException):
    """Unauthorized error exception"""
    def __init__(self, detail: str = "Unauthorized"):
        super().__init__(detail, 401, "UNAUTHORIZED")

class ForbiddenError(AppException):
    """Forbidden error exception"""
    def __init__(self, detail: str = "Forbidden"):
        super().__init__(detail, 403, "FORBIDDEN")
