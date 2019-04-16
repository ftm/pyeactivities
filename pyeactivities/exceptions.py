class APIException(Exception):
    pass


class APIUnauthorisedException(APIException):
    pass


class APIForbiddenException(APIException):
    pass
