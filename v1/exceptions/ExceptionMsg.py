# coding=utf-8


class ExceptionMsg:
    def __init__(self):
        pass
    """
    
    """
    @staticmethod
    def set_message_error(code=int, msg=str, options=object):
        return {
            "code": code,
            "msg": msg,
            "options": options
        }

    @staticmethod
    def message_to_session_invalid():
        return {
            "code": 11001,
            "msg": "Token or session is invalid.",
            "options": ["Replace token for new token.", "Login."]
        }

    @staticmethod
    def message_to_object_not_found():
        return {
            "code": 11002,
            "msg": "Object not found.",
            "options": ["Replace the Id."]
        }

    @staticmethod
    def message_to_json_invalid():
        return {
            "code": 11003,
            "msg": "Json body id invalid.",
            "options": ["Replace json object.", "See documentation."]
        }

    @staticmethod
    def message_to_bad_request(message):
        return {
            "code": 11014,
            "msg": "Bad request.",
            "errors": message,
            "options": ["Replace json object or parameters.", "Resend petition", "See documentation."]
        }

    @staticmethod
    def message_to_bad_token_client():
        return {
            "code": 11015,
            "msg": "Client token not valid.",
            "options": ["Replace token client.", "See documentation.", "Report error to admin of application."]
        }

    @staticmethod
    def message_to_not_content():
        return {
            "code": 11016,
            "msg": "Not content",
            "options": ["Replace body of request.", "See documentation."]
        }

    @staticmethod
    def message_to_not_json():
        return {
            "code": 11017,
            "msg": "Not content json or not found header 'Content-Type:application/json'. ",
            "options": ["Replace body of request.", "Include header 'Content-Type:application/json'.",
                        "See documentation."]
        }

    @staticmethod
    def message_to_page_not_found():
        return {
            "code": 11018,
            "msg": "Page not found.",
            "options": ["See documentation."]
        }

    @staticmethod
    def message_to_method_not_allowed():
        return {
            "code": 11019,
            "msg": "Method not allowed.",
            "options": ["See documentation."]
        }

    @staticmethod
    def message_to_credentials_invalid():
        return {
            "code": 11010,
            "msg": "User or password is invalid.",
            "options": ["Resend petition."]
        }

    @staticmethod
    def message_to_server_error(message):
        return {
            "code": 11011,
            "msg": "Error in server, message=" + message,
            "options": ["Report error to admin of application.", "Resend petition"]
        }

