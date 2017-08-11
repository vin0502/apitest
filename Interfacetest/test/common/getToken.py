#__author__ = 'pan'
# -*- coding:utf-8 -*-

import requests
from utils.log import Log


logger = Log()

def gettoken(url,username,password):
    '''登陆'''
    # 使用ruquests.session()绕过验证码
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    # 创建一个session
    session = requests.session()
    # update session 的头
    session.headers.update(header)
    payload = {
        "username": username,
        "password": password,
        # "key": "0.8261895872254148app",
        # "capchat": ""
    }
    response = session .post(url, payload)
    print(response.text)
    hjson = response.json()  # 获取并处理返回的json数据
    herror = "error"
    if herror in hjson:
        logger.info("登陆失败，退出程序！")
        exit()
    else:
        hcode = str(hjson['code'])
        logger.info('请求返回状态为：' + hcode)
        if hcode == '0':
            token = hjson['data']['token']  # 获取token
            logger.info('当前token为：' + token)
            return  token
        else:
            logger.info("登陆失败，退出程序！")
            exit()

if __name__ == '__main__':
    url = 'http://106.75.3.62:8887/tms/app/approval/login'
    gettoken(url,'pengda','111111')