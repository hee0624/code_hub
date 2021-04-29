#!/usr/bin/env python
# coding=utf-8


from zeep import Client

client = Client('http://{0}:{1}/?wsdl'.format('127.0.0.1', 7789))
factory = client.type_factory('ns0')
pro1 = factory.Project(name='p1', version='v0')
pro2 = factory.Project(name='p2', version='v1')
pros = factory.ProjectArray([pro1, pro2])
print(client.service.show_project(pros))




