# -*- coding: utf-8 -*-
import re


# route data

class Router(object):
    static_router = {}

    dynamic_router = {
        'GET': {},
        'POST': {},
        'PUT': {},
        'DELETE': {}
    }

    @classmethod
    def match(cls, method: str, url: str):
        # match static router
        if (method, url) in cls.static_router.keys():
            return cls.static_router[(method, url)].controller, None
        # match dynamic router
        for url in cls.dynamic_router[method].keys():
            pattern = re.compile(r'%s' % (url), re.I)
            match = pattern.match(url)
            if match is None:
                continue
            pattern_list = cls.dynamic_router[method][url]['pattern_list']
            length = len(match.groups())
            pattern_dict = {}
            for i in range(length):
                pattern_dict[pattern_list[i]] = match.groups()[i]
            return cls.dynamic_router[method][url]['controller'], pattern_dict

        return None, None
