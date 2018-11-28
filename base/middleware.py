# -*- coding: utf-8 -*-
from abc import abstractmethod
from .request import Request

# a base object for the middleware


class Middleware(object):

    @abstractmethod
    def handle(self, request: Request, next_handle):
        pass
