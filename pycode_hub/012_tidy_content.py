# coding:utf-8
"""
@desc: 处理ocr之后的内容，整理成完整的语义段落
@author: chenhe
@create: 2018年 12月 19日 星期三 09:24:52 CST
"""

import re
import jieba


def tidy_content(ori_content, line_num=24):
    """
    处理ocr之后的内容，整理成完整的语义段落
    :param ori_content: 待整理的内容,类型为string
    :return fmt_content: 格式为string
    """
    lines_blank = []
    lines_title = []
    lines_merge = []
    lines_res = []
    word_dic = set()
    with open('dict.txt') as fp:
        for line in fp:
            if line.strip():
                word = line.split(' ')[0]
                word_dic.add(word)
    lines = ori_content.split('\n')
    tmp = []
    lines.insert(0, '')
    lines.insert(1, '')
    # 处理标题分开
    for ix, line in enumerate(lines):
        line = line.strip()
        if re.match('\s*[\(（]?\s*[0-9一二三四五六七八九十]+[\)）]?\s*[、：:]?$', line):
            print(line)
            tmp.append(line)
        else:
            if tmp:
                tmp.append(line)
                bind_line = ''.join(tmp)
                bind_line = bind_line.replace('\n', '')
                lines_title.append(bind_line)
                tmp.clear()
            else:
                lines_title.append(line)
    # 遇到小标题，上下行添加空白行
    for ix, line in enumerate(lines_title):
        line = line.strip()
        if re.match('\s*\d+\s*\.', line):
            lines_blank.append('')
            lines_blank.append(line)
        elif re.match('\s*[\(（]\s*[\d\w]+\s*[\)）]', line):
            lines_blank.append('')
            lines_blank.append(line)
        elif re.match('\w{2,7}\s*[:：]', line):
            lines_blank.append('')
            lines_blank.append(line)
        elif re.match('^.*?[:：]$', line):
            lines_blank.append(line)
            lines_blank.append('')
        else:
            try:
                front_line = lines[ix-1]
                if re.match('^(.*?[。？！]\s*)$', front_line):
                    lines_blank.append('')
                    lines_blank.append(line)
                else:
                    lines_blank.append(line)
            except IndexError:
                lines_blank.append(line)
    # 合并段落
    tmp = []
    for line in lines_blank:
        num = len(line)
        if num >= line_num and not tmp:
            tmp.append(line)
        elif num <= line_num and tmp:
            tmp.append(line)
            lines_merge.append(''.join(tmp))
            tmp.clear()
        elif num >= line_num and tmp:
            tmp.append(line)
        else:
            lines_merge.append(line)
    else:
        if tmp:
            lines_merge.append(''.join(tmp))
    # 处理行尾与下一行是一个词
    try:
        end_word = list(jieba.cut(lines_merge[0]))[-1]
        lines_res.append(lines_merge[0])
    except IndexError:
        end_word = ''
        lines_res.append('')
    for line in lines_merge[1:]:
        tmp = end_word
        seg_list = list(jieba.cut(line))
        if seg_list:
            first_word = seg_list[0]
            end_word = seg_list[-1]
            word = tmp + first_word
            if tmp in [',', '，', ';']:
                last_line = lines_res.pop()
                bind_line = last_line + line
                lines_res.append(bind_line.replace('\n', ''))
            elif len(first_word) == 1 and (word in word_dic):
                last_line = lines_res.pop()
                bind_line = last_line + line
                lines_res.append(bind_line.replace('\n', ''))
            else:
                lines_res.append(line)
        else:
            lines_res.append(line)
    fmt_lst = []
    for ix, line in enumerate(lines_res):
        if line.strip():
            fmt_lst.append(line)
        print(ix, line)
    fmt_content = '\n'.join(fmt_lst)
    return fmt_content


if __name__ == '__main__':
    text = """
信用卡中心财务管理委员会通知书
客户服务部:
经信用卡中心财务管理委员会二O一七年第二十四次会议(2017年
12月01日)表决通过贵部门以下议题:
议题:客户服务部关于建设外交部全球领事保护与服务应急呼叫中
心手机APP的请示(2014年，信用卡中心代装民生银行代维代建了“外
交部全球领事保护与服务应急呼叫中心”(简称“呼叫中心”)，并于当年
3月2日正式运营，面向全球华人开放。根据形势发展需要，外交部拟
将借力信息技术和新媒体传播优势，外交部在2016年的招标文件中要求
新建基于APP的多媒体服务求助平台，实现与呼叫中心系统的无缝对接，
并计划在2017年推出12308手机APP，在提供高质量政府服务的同时，
追求与移动互联网发展节奏-一致的高质量用户体验。计划于2018年1月
31曰前完成系统上线。
经卡中心科技管理部评估，此项目费用共约148.8万元。费用具体
明细如下:
贵别预算跳用工 贷源配登方式
佻应谢
硬件:
251元科技标准产 品

    """
    # with open('result.txt', 'r') as fp:
    #     text = fp.read()
    print(tidy_content(ori_content=text))
