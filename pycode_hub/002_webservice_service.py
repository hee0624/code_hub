#!/usr/bin/env python
# coding=utf-8

__author__ = 'chenhe'
__version__ = '0.1'

"""
createdate: 2018-03-08
comment: webservice简单学习, soaplib不再维护，转向spyne
"""

from spyne import Application, rpc, ServiceBase
from spyne import Integer, Unicode, Array, ComplexModel, Iterable
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server


class Project(ComplexModel):
    name = Unicode
    version = Unicode


class HelloWorldService(ServiceBase):
    @rpc(Unicode, Integer, _returns=Array(Unicode))
    def say_hello(self, name, times):
        results = []
        for i in range(0, times):
            results.append('Hello {0}'.format(name))
        return results

    @rpc(Project, _returns=Unicode)
    def make_project(self, pro):
        return '{0}+{1}'.format(pro.name, pro.version)

    @rpc(Array(Project), _returns=Iterable(Unicode))
    def show_project(self, pros):
        if not pros:
            yield 'None'
        for pro in pros:
            yield pro.name + pro.version


if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.INFO)
    try:
        soap_app = Application(
            [HelloWorldService],
            'SampleServices',
            in_protocol = Soap11(validator='lxml'),
            out_protocol = Soap11()
            )
        wsgi_app = WsgiApplication(soap_app)
        server = make_server('localhost', 7789, wsgi_app)
        logging.info('server starting ......')

        server.serve_forever()
    except Exception as e:
        logging.excepting(e)

