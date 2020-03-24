# coding=utf-8
from __future__ import print_function
import builtins
import traceback
import datetime
__base_print = print


def nb_print(func):
    def wrapper(*args, **kwargs):
        nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在
        # print(nowTime)
        func(*args, **kwargs,end=' ')
        __base_print(nowTime)

    return wrapper


builtins.print = nb_print(print)

if __name__ == '__main__':
    print('http://www.baidu.com')