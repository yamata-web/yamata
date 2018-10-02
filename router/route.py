# -*- coding: utf-8 -*-

# a single route instance

class Route(object):
    '''
    Create a route instance.
    @param  string  url
    @param  string  controller
    @param  string  method
    @param  list  middleware_group
    @param  list  personal_middleware
    @return void
    '''

    def __init__(self, url, controller, method, middleware_group=None, personal_middleware=None):
        self.url = url
        self.controller = controller
        self.method = method
        if middleware_group:
            self.middleware_group = middleware_group
        else:
            self.middleware_group = []
        if personal_middleware:
            self.personal_middleware = personal_middleware
        else:
            self.personal_middleware = []
        self.name = ''

    '''
    Setting a middleware for this route.
    @param  string  middleware
    @return void
    '''

    def middleware(self, middleware):
        self.personal_middleware.append(middleware)

    '''
    Setting a name for this route.
    @param  string  name
    @return void
    '''

    def name(self, name):
        self.name = name
