# __author__ = 'pan'
#coding=utf-8

import hashlib
import urllib.parse

def getParam(param):
    '''
    封装get请求的参数拼接形式
    :param param: 请求参数
    :return: 拼接好的参数串
    '''
    #获取键，即参数名
    paramk = param.keys()
    #按照键值字典序由小到大排列
    paramk.sort()
    params = ''
    for i in paramk:
        #获取键值
        kvalue = param.get(i)
        #按照key1=value1key2=value2的方式拼接，没有分隔符
        params = '{0}{1}={2}'.format(params,i,kvalue)
    #调用签名方法
    sign =paramSign(params)
    #加入参数sign
    param['sign'] = sign
    #拼接参数，格式a=1&b=2
    paramStr = urllib.parse.urlencode(param)
    return paramStr

def postParam(param):
    '''
    封装post请求的参数拼接形式
    :param param: 请求参数
    :return: 拼接好的参数串
    '''
    #获取键，即参数名
    paramk = param.keys()
    #按照键值字典序由小到大排列
    paramk.sort()
    params = ''
    for i in paramk:
        #获取键值
        kvalue = param.get(i)
        #按照key1=value1key2=value2的方式拼接，没有分隔符
        params = '{0}{1}={2}'.format(params,i,kvalue)
    #调用签名方法
    sign =paramSign(params)
    #加入参数sign
    param['sign'] = sign
    return param

def paramSign(params):
    '''
    :param params: 按照key1=value1key2=value2的方式拼接的参数串
    :return: 返回最终的签名值sign
    '''
    m1 = hashlib.md5()
    #参数必须是byte类型，否则报Unicode-objects must be encoded before
    m1.update(params)
    #首次对拼接结果取一次MD5
    sign1 = m1.hexdigest()
    #将md5结果尾部拼接渠道的私钥内容
    sign2 = '{0}{0}'.format(sign1,'a')
    m2 =  hashlib.md5()
    m1.update(sign2)
    #对拼接结果再做一次md5加密
    sign = m2.hexdigest()
    return sign