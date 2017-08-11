# __author__ = 'pan'
# -*- coding:utf-8 -*-

import json
import requests
from test.common import parameter


#定制特殊request请求

def get_request(url,param):
    '''封装get请求'''
    #拼接请求
    r_url = url + '?' + parameter.getParam(param)
    #发送请求
    request = requests.get(r_url)
    #获取返回值
    response = request.text
    #将返回值转化为python可识别的dict对象
    json_response = json.loads(response)
    return json_response

def post_request(url,param):
    '''封装post请求'''
    #发送请求
    request = requests.post(url, parameter.postParam(param))
    #获取返回值
    response = request.text
    #将返回值转化为python可识别的dict对象
    json_response = json.loads(response)
    return json_response