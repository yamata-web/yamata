# -*- coding: utf-8 -*-
from abc import abstractmethod


class Middleware(object):

    @abstractmethod
    def handle(self, request, next_handle):
        pass
