import json


class dct(object):
    def __init__(self, j):
        self.__dict__ = json.load(j)
