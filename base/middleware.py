# -*- coding: utf-8 -*-
from abc import abstractmethod

# a base object for the middleware
class Middleware(object):

    @abstractmethod
    def handle(self, request, next_handle):
        pass