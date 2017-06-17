# coding=utf-8
from v1.resources.Controller import Controller


class TestController(Controller):
    def __init__(self):
        super(TestController, self).__init__()

    def get(self):
        print "hello world"
        return {'hello': 'world', "controller": "Test"}