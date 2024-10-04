class CustomException(Exception):
    def __init__(self, status_code: int, detail: str):
        self.status_code = status_code
        self.detail = detail


class DatabaseException(CustomException):
    pass


class APIException(CustomException):
    pass
