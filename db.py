import json


class Db(object):
    def __init__(self, j):
        self.__dict__ = json.load(j)
