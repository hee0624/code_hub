#!/usr/bin/env python
# coding=utf-8

from datetime import datetime
from datetime import timedelta


# 获取一段时间的工作日
def get_work_date_list(begin_date, end_date):
    dates = []
    dt = datetime.strptime(begin_date, '%Y-%m-%d')
    date = begin_date[:]
    while date <= end_date:
        if dt.strftime('%w') in ['1', '2', '3', '4', '5']:
            dates.append(date)
        dt += timedelta(days=1)
        date = dt.strftime('%Y-%m-%d')
    return dates


# 获取一段时间的时间列表
def get_date_list(begin_date, end_date):
    dates = []
    dt = datetime.strptime(begin_date, '%Y-%m-%d')
    date = begin_date[:]
    while date <= end_date:
        dates.append(date)
        dt += timedelta(days=1)
        date = dt.strftime('%Y-%m-%d')
    return dates
