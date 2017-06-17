class HTTP:
    # 2xx
    OK = 200
    CREATED = 201
    NO_CONTENT = 204
    UNPROCESSABLE_ENTITY = 422

    # 4xx
    BAD_REQUEST = 400
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    CONFLICT = 409

    # 5xx
    INTERNAL_SERVER_ERROR = 500
    SERVICE_UNAVAILABLE = 503

    def __init__(self):
        pass
