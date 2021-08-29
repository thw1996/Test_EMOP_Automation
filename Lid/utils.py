import json
import logging
import time
import random

def json2dict(json_string):
    if json_string:
        try:
            return json.loads(json_string)
        except json.decoder.JSONDecodeError:
            logging.error("json格式错误: {}".format(json_string))

def throw_error(error):
    """抛出异常"""
    raise Exception(error)

def retry(times=3,wait_time=10):
    """出错用例重跑"""
    def warp_func(func):
        def fild_retry(*args,**kwargs):
            for t in range(times):
                try:
                    func(*args,**kwargs)
                    return
                except:
                    time.sleep(wait_time)
        return fild_retry
    return warp_func
def create_phone():
    # 第二位数字
    second = [3, 4, 5, 7, 8][random.randint(0, 4)]

    # 第三位数字
    third = {
        3: random.randint(0, 9),
        4: [5, 7, 9][random.randint(0, 2)],
        5: [i for i in range(10) if i != 4][random.randint(0, 8)],
        7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
        8: random.randint(0, 9),
    }[second]

    # 最后八位数字
    suffix = random.randint(9999999,100000000)

    # 拼接手机号
    return "1{}{}{}".format(second, third, suffix)