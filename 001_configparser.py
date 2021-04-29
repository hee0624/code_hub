# coding=utf-8
# author: chenhe<hee0624@163.com>
# time: 2017-09-13
# version: v0.0
import configparser


def w_config():
    """写入配置文件"""
    config = configparser.ConfigParser()
    config['fig1'] = {
        't1': True,
        't2': 'test2',
        't3': 1234,
        't4': 1.23
    }
    config['fig2'] = {
        't1': 'test',
        't2': True,
        't3': 2017.7
    }
    with open('my.conf', 'w') as configfile:
        config.write(configfile)

def r_config():
    """读取配置文件"""
    config = configparser.ConfigParser()
    config.read('my.conf')
    print(config.sections())
    print(config['fig1'].getboolean('t1'))
    print(config['fig1'].get('t2'))
    print(config['fig1'].getint('t3'))
    print(config['fig1'].getfloat('t4'))


if __name__ == "__main__":
    # w_config()
    r_config()