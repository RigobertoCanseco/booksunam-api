# coding=utf-8
from v1 import app, db, api

from v1.resources.TestController import TestController


api.add_resource(TestController, '/')


# @app.route('/')
# def index():
#     return render_template('index.html')
#
#
# @app.route('/<path:resource>')
# def serve_static_resource(resource):
#     return send_from_directory('static/', resource)


if __name__ == '__main__':
    app.run(app.config['IP'], app.config['PORT'])
