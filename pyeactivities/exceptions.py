class APIException(Exception):
    """
    The base class for any exception thrown by pyeactivities relating to the
    eActivities API
    """

    pass


class APIUnauthorisedException(APIException):
    """
    This exception is thrown by any API access that results in the eActivites API
    returning a 401 Unauthorised status code. The most likely cause is normally
    an incorrect API key.
    """

    pass


class APIForbiddenException(APIException):
    """
    This exception is thrown by and API access that results in the eActivities API
    returning a 403 Forbidden status code. The most likely cause is too many
    requests with an incorrect API key, or an excessive number of requests.
    """

    pass
