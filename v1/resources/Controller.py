from flask_restful import Resource
from v1 import app, auth


# HANDLERS
# NOT_FOUND
@app.errorhandler(404)
def page_not_found(a):
    return "NOT FOUND", 404


# METHOD_NOT_ALLOWED
@app.errorhandler(405)
def method_not_allowed(a):
    return "METHOD_NOT_ALLOWED", 405


users = {
    "admin": "secret"
}


@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None


@app.route('/secret-page')
@auth.login_required
def index():
    return "Hello, %s!" % auth.username()


class Controller(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        super(Controller, self).__init__()


class ControllerList(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        super(ControllerList, self).__init__()