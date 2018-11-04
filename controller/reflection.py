# -*- coding: utf-8 -*-
import inspect
import app.controller

class Reflection(object):
    @staticmethod
    def reflect(str: str):
        className, method = str.split('@')
        # new class
        classObj = eval(className)()
        # get class method
        funcObj = getattr(classObj, method)
        # get function arg
        arglist = inspect.getfullargspec(funcObj)
        argdict = {}
        # new arg class and add to argdict
        for key in arglist.args:
            if key in arglist.annotations:
                argdict[key] = arglist.annotations[key]()
        return funcObj(**argdict)