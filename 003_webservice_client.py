#!/usr/bin/env python
# coding=utf-8



from suds.client import Client

client = Client('http://{0}:{1}/?wsdl'.format('127.0.0.1', 7789))
print(client)
result = client.service.say_hello(name='chenhe', times=8)
print(result)

# 针对复杂数据类型

# 第一种方式调用
project = client.factory.create('Project')
project.name = 'Test'
project.version = '1.0.0'
print(client.service.make_project(project))


# 第二种方式调用

project = {'name': 'Test2', 'version': '2.0.0'}
print(client.service.make_project(project))


# 针对数组类型

projects = client.factory.create('ProjectArray')
project = client.factory.create('Project')
project.name = 'Test'
project.version = '1.0.0'
projects.Project.append(project)
projects.Project = [{'name':'v1', 'version': 'v1'}, {'name': 'v2', 'version': 'v2'}]

print(client.service.show_project(projects))



