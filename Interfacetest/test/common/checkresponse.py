#__author__ = 'pan'
# -*- coding:utf-8 -*-


import re
import operator

class ResultCheck(object):
    """
    检查接口返回结果
    class to check result:
    This class is used to check the results returned by the interface. Parameters must be dictionary type.
    """
    def __init__(self):
        pass

    @staticmethod
    def CmpOutPara(ActualResultDict, ExpectResultDict):
        '''
        检查接口出参是否与预期结果中的参数一致，包含参数名、参数数量
        :param ActualResultDict:
        :param ExpectResultDict:
        :return:
        '''
        KeyActualResultDict = ActualResultDict['response'].keys()
        KeyExpectResultDict = ExpectResultDict['response'].keys()
        # 检查参数是否一致
        if operator.eq(KeyActualResultDict, KeyExpectResultDict) != True:
            if len(KeyExpectResultDict) > len(KeyActualResultDict):
                InterfaceParaMessage = '返回结果中缺少参数'
                return False, InterfaceParaMessage
            elif len(KeyExpectResultDict) < len(KeyActualResultDict):
                InterfaceParaMessage = '返回结果中多传了参数'
                return False, InterfaceParaMessage
            else:
                InterfaceParaMessage = '返回结果以下参数不正确:'
                for i in range(len(KeyExpectResultDict)):
                    if KeyExpectResultDict[i] not in KeyActualResultDict[i]:
                        InterfaceParaMessage += '、' + KeyExpectResultDict[i]
                return False, InterfaceParaMessage
        else:
            InterfaceParaMessage = '返回的参数正确'
            return True, InterfaceParaMessage

    @staticmethod
    def AllOutValue(ActualResultDict, ExpectResultDict):
        '''#all模式'''
        if operator.eq(str(ActualResultDict['response']), str(ExpectResultDict['response'])) == 0:
            InterfaceMessage = '接口返回的结果完全正确'
            InterfaceStatus = True
            return InterfaceStatus, InterfaceMessage
        else:
            InterfaceMessage = '接口返回的结果不完全正确'
            InterfaceStatus = False
            return InterfaceStatus, InterfaceMessage

    @staticmethod
    def partOutValue(ActualResultDict, ExpectResultDict):
        '''part模式'''
        bCmpResult = -1
        message = ""
        expectResultDict = ExpectResultDict['response']
        actualResultDict = ActualResultDict['response']
        for key, value in expectResultDict.items():
            if actualResultDict[key] == value:
                bCmpResult, message = 1, "test pass"
            else:
                bCmpResult, message = 0, "test fail" + "actual result: " + actualResultDict[key] + "expect result: " + value
                break
        return (bCmpResult, message)

    @staticmethod
    def assertnotnull(ActualResultStr):
        '''检查接口参数值是否存在null'''
        matchResult = re.findall('null', ActualResultStr, re.IGNORECASE)
        if matchResult:
            return False
        else:
            return True

if __name__ == '__main__':

    a = {'status': 200, 'response': {'a': 2, 'messagee': {'c': 'asd'}, 'c': 'as'}}
    b = {'type': 'part', 'response': {'a': 2, 'c': 'asd'}}
    c = {'status': 200, 'message': 2, 'a': 2, 'messagee': 3}
    aaa = ResultCheck()
    (ResultStatus, ResultStatusMessage) = aaa.CmpOutPara(a, b)
    print(ResultStatus, ResultStatusMessage)
