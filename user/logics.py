import re
import random
from TT import config
import requests
from common import keys
from django.core.cache import cache

def is_phonenum(phonenum):
    '''检查是否是一个正常的手机号'''
    if re.match(r'1[2345678]\d{9}$', phonenum):
        return True
    else:
        return False


def get_random_code(length=4):
    '''产生一个指定长度的手机验证码'''
    rand_num = random.randrange(0, 10 ** length)
    template = '%%0%sd' % length
    vcode = template % rand_num
    return vcode

def send_msg(phonenum, vcode):
    '''发送短信'''
    args = config.params.copy()  #原型模式
    args['param'] = vcode
    args['mobile'] = phonenum

    response = requests.post(config.msg_url, json=args)
    return response

def sned_vcode(phonenum):
    '''发送验证码'''
    vcode = get_random_code(4)  #产生一个随机的验证码
    print('--------------->', vcode)
    response = send_msg(phonenum, vcode)     #发送验证码

    if response.status_code == 200:
        result = response.json()
        if result.get('code') == '000000':
            # 将验证码发送到缓存
            key = keys.VCODE_KEY % phonenum
            cache.set(key, vcode, 180)
            return True
    return False
