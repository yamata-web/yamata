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

    '''
    match a url in static_router or dynamic_router,
    if matched static_router, return route instance and none
    if matched dynamic_router, return route instance and pattern_dict
    if not return none and none
    @param  str  method
    @param  str  url
    @return route instance
    @return dict pattern_dict
    '''
    @classmethod
    def match(cls, method: str, url: str):
        # match static router
        url = Router.revise_url(url)
        print(url)
        print(method)
        if (method, url) in cls.static_router.keys():
            return cls.static_router[(method, url)], None
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
            return cls.dynamic_router[method][url], pattern_dict

        return None, None

    @staticmethod
    def revise_url(url: str):
        if url is None:
            return ''
        url = '/' + url.strip('/') + '/'
        return url

    @staticmethod
    def revise_namespace(namespace: str):
        if namespace is None:
            return ''
        namespace.strip('.') + '.'
        return namespace
