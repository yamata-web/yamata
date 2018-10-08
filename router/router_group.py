# -*- coding: utf-8 -*-
import copy
import re
from .route import Route
from .router import Router


# route data manger

class RouterGroup(object):

    def __init__(self, middleware_group=None, prefix=None, namespace=None):
        self.middleware_group_list = []
        if middleware_group:
            self.middleware_group_list.append(middleware_group)
        self.prefix = RouterGroup.revise_prefix(prefix)
        self.namespace = RouterGroup.revise_namespace(namespace)

    @staticmethod
    def revise_prefix(prefix: str):
        if prefix is None:
            return ''
        prefix.strip('/') + '/'
        return prefix

    @staticmethod
    def revise_namespace(namespace: str):
        if namespace is None:
            return ''
        namespace.strip('.') + '.'
        return namespace

    def group(self, middleware_group=None, prefix=None, namespace=None):
        router_group = copy.deepcopy(self)
        if middleware_group:
            router_group.middleware_group_list.append(middleware_group)
        router_group.prefix += RouterGroup.revise_prefix(prefix)
        router_group.namespace += RouterGroup.revise_namespace(namespace)
        return router_group

    '''
    add a get route in static_router or dynamic_router
    @param  str  url
    @return str  controller
    @return void
    '''
    def get(self, url: str, controller: str):
        self.add_route(url, controller, 'get')

    '''
    add a post route in static_router or dynamic_router
    @param  str  url
    @return str  controller
    @return void
    '''
    def post(self, url: str, controller: str):
        self.add_route(url, controller, 'post')

    '''
    add a put route in static_router or dynamic_router
    @param  str  url
    @return str  controller
    @return void
    '''
    def put(self, url: str, controller: str):
        self.add_route(url, controller, 'put')

    '''
    add a delete route in static_router or dynamic_router
    @param  str  url
    @return str  controller
    @return void
    '''
    def delete(self, url: str, controller: str):
        self.add_route(url, controller, 'delete')

    '''
    add a route in static_router or dynamic_router.
    @param  str  url
    @return str  controller
    @param  str  method
    @return void
    '''
    def add_route(self, url: str, controller: str, method: str):
        url = ''.join(['/', self.prefix, url.strip('/'), '/'])
        controller = ''.join(['.', self.namespace, controller.strip('.')])
        pattern = re.compile(r'(\$\w+)/')
        length = len(pattern.findall(url))
        if length > 0:
            url = re.sub(pattern, '(\w+?)/', url)
            Router.dynamic_router[method][url] = {
                'route': Route(url, controller, method, self.middleware_group_list),
                'pattern_list': pattern.findall(url)
            }
        else:
            Router.static_router[(method, url)] = Route(url, controller, method, self.middleware_group_list)
