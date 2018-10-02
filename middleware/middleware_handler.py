# -*- coding: utf-8 -*-
from .iterator import Iterator


class MiddlewareHandler(object):
    middleware = [

    ]

    middleware_groups = {

    }

    route_middleware = {

    }

    @classmethod
    def init(cls, middleware, middleware_groups, route_middleware):
        cls.middleware = middleware
        cls.middleware_groups = middleware_groups
        cls.route_middleware = route_middleware

    @staticmethod
    def handle_global_middleware(request):
        if len(MiddlewareHandler.middleware) > 0:
            return MiddlewareHandler.middleware[0](
                request, Iterator(MiddlewareHandler.middleware).next
            )

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
