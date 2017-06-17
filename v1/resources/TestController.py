# coding=utf-8
from flask_restful import Resource


class TestController(Resource):
    def get(self):
        print "hello world"
        return {'hello': 'world', "controller": "Test"}