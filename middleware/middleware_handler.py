# -*- coding: utf-8 -*-
from .iterator import Iterator


class MiddlewareHandler(object):
    # global middleware
    middleware = [

    ]

    # groups middleware
    middleware_groups = {

    }

    # signal middleware
    route_middleware = {

    }

    '''
    when the server first run, init the middleware data.
    @param  list  middleware
    @param  dict  middleware_groups
    @param  dict  route_middleware
    @return void
    '''
    @classmethod
    def init(cls, middleware, middleware_groups, route_middleware):
        cls.middleware = middleware
        cls.middleware_groups = middleware_groups
        cls.route_middleware = route_middleware

    '''
    run the global middleware.
    @param  Request request
    @return Request or Response 
    '''
    @staticmethod
    def handle_global_middleware(request):
        if len(MiddlewareHandler.middleware) > 0:
            return MiddlewareHandler.middleware[0](
                request, Iterator(MiddlewareHandler.middleware).next
            )

    '''
    run the group middleware and the personal middleware for a route.
    @param  Request request
    @return Request or Response 
    '''
    @staticmethod
    def handle_middleware_for_route(request, route):
        for key in route.middleware_group:
            middleware = MiddlewareHandler.middleware_groups[key]
            request = middleware[0](request, Iterator(middleware).next)
        middleware = []
        for key in route.personal_middleware:
            middleware.append(MiddlewareHandler.route_middleware[key])
        if len(middleware) > 0:
            return middleware[0](request, Iterator(middleware).next)
        else:
            return request
