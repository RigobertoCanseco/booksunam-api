# coding=utf-8
import datetime


# code
exc =\
    dict(
        x1=dict(
            x00=dict(
                x00=dict(
                    code=10000,
                    msg="Se esperan un objeto en el cuerpo de la petición"
                )
            )
        ),
        x2=dict(
            x00=dict(
                x00=dict(
                    code=20000,
                    msg="Se esperan un objeto en el cuerpo de la petición"
                )
            )
        ),
        x3=dict(
            x00=dict(
                x00=dict(
                    code=30000,
                    msg="Se esperan un objeto en el cuerpo de la petición"
                )
            )
        ),
        x4=dict(
            x00=dict(
                x00=dict(
                    code=40000,
                    msg="Se esperan un objeto en el cuerpo de la petición"
                )
            )
        ),
        x5=dict(
            x00=dict(
                x00=dict(
                    code=50000,
                    msg="Se esperan un objeto en el cuerpo de la petición"
                )
            )
        )
    )


exception = {
    "bad_request": {
        "code": 100000,
        "msg": "Se esperan un objeto en el cuerpo de la petición",
        "options": [
            "Intentar de nuevo"
        ]
    },
    "not_json": {
        "code": 100001,
        "msg": "Se esperan Content-Type:application/json ",
        "options": [
            "Intentar de nuevo"
        ]
    },
    "invalid_element": {
        "code": 100002,
        "msg": "Falta un elemento en el objeto:",
        "options": [
            "Intentar de nuevo"
        ]
    },
    "method_invalid": {
        "code": 100000,
        "msg": "Metódo no permitido",
        "options": [
            "Intentar de nuevo"
        ]
    }

}


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
    def get_message_error(e=object):
        return exception[e]
