# coding: utf-8
"""
@Author  : ChenHe
@Time    : 4/29/21 4:31 PM
@File    : auto_code.py
@Software: PyCharm
@Github  ： https://github.com/hee0624
@Description:
"""


import json
import codecs


def auto_code(out_path, config_path='config.json', template_path='template.txt'):
    # read config file
    config = {}
    with codecs.open(config_path, 'rb', 'UTF-8') as fp:
        config = json.loads(fp.read())
    if not config:
        return
    # read template file
    s = ""
    with codecs.open(template_path, 'rb', 'UTF-8') as f:
        s = f.read()
    if not s:
        return
    s = s % config
    # save to file
    with codecs.open(out_path, "wb", "UTF-8") as f:
        f.write(s)
        f.flush()


if __name__ == '__main__':
    try:
        auto_code(out_path='auto_template.py')
    except Exception as ex:
        print(ex)
