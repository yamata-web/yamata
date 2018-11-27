# -*- coding: utf-8 -*-
from yamata.base.request import Request


class Iterator(object):
    def __init__(self, middleware, index=0):
        self.index = index
        self.middleware = middleware

    def next(self, request: Request):
        self.index += 1
        if self.index < len(self.middleware):
            return self.middleware[self.index](request, self.next)
        else:
            return request
