# -*- coding: utf-8 -*-


class Request(object):
    def __init__(self, env):
        self.env = env
        self.method = env['REQUEST_METHOD']
        self.url = env['REQUEST_URI']
        self.parameter = {}
        if 'REQUEST_URI' in env.keys():
            self.parameter_init(env['REQUEST_URI'])

    def parameter_init(self, http_referer):
        parameter_list = http_referer.split('?')
        if len(parameter_list) > 1:
            parameter_list = parameter_list[1].split('&')
            for parameter in parameter_list:
                pairs = parameter.split('=')
                self.parameter[pairs[0]] = pairs[1]
