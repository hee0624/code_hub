#!/usr/bin/env python
# coding=utf-8

# 字符处理转成unicode
word_dic = {u'研究', u'研究生', u'生命', u'命', u'的', u'起源'}

def max_forward_cut(sent):
    """正向最大匹配法"""
    res = []
    sent_len = len(sent)
    max_word_len = 5
    index = 0
    while index < sent_len:
        for ix in range(max_word_len, 0, -1):
            cut_word = sent[index: index+ix]
            if  cut_word in word_dic:
                res.append(cut_word)
                break
            else:
                pass
        else:
            res.append(sent[index])
        index += ix
    #print('/'.join(res))
    return res


def max_backward_cut(sent):
    """逆向最大匹配法"""
    res = []
    sent_len = len(sent)
    max_word_len = 5
    index = sent_len
    while index > 0:
        for ix in range(max_word_len, 0, -1):
            cut_word = sent[index-ix: index]
            if  cut_word in word_dic:
                res.append(cut_word)
                break
            else:
                pass
        else:
            res.append(sent[index-1])
        index -= ix
    #print('/'.join(res[::-1]))
    return res[::-1]

def max_biward_cut(sent):
    """正切/逆向都切分一遍，然后根据大颗粒度词越多越好,总词数越少越好,非词典词和单字词越少越好"""
    def compute_single(lst):
        num = 0
        for i in lst:
            if len(i) == 1:
                num += 1
        return num
    forward_lst = max_backward_cut(sent)
    backward_lst = max_backward_cut(sent)
    forward_lst_len = len(forward_lst)
    backward_lst_len = len(backward_lst)
    forward_sig_len = compute_single(forward_lst)
    backward_sig_len = compute_single(backward_lst)
    if backward_lst_len < forward_lst_len:
        return backward_lst
    elif backward_lst_len > forward_lst_len:
        return forward_lst
    else:
        if backward_sig_len < forward_sig_len:
            return backward_lst
        elif backward_sig_len > forward_lst_len:
            return forward_lst
        else:
            return backward_lst



if __name__ == '__main__':
    r = max_forward_cut(u'我研究生命的起源')
    print('/'.join(r))
    r =max_backward_cut(u'我研究生命的起源')
    print('/'.join(r))
    r =max_biward_cut(u'我研究生命的起源')
    print('/'.join(r))

