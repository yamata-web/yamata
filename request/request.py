# -*- coding: utf-8 -*-


class Request(object):

    '''
    Create a request instance.
    @param  dict  env
    @return void
    '''
    def __init__(self, env):
        self.env = env
        self.method = env['REQUEST_METHOD']
        self.url = env['REQUEST_URI']
        self.parameter = {}
        if 'REQUEST_URI' in env.keys():
            self.parameter = self.parameter_init(env['REQUEST_URI'])

    '''
    split a url parameter to dict.
    @param  str  http_referer
    @return dict parameter
    '''
    def parameter_init(self, http_referer):
        parameter = {}
        parameter_list = http_referer.split('?')
        if len(parameter_list) > 1:
            parameter_list = parameter_list[1].split('&')
            for parameter in parameter_list:
                pairs = parameter.split('=')
                parameter[pairs[0]] = pairs[1]
        return parameter
