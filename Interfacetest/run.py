# __author__ = ‘pan‘
# -*-coding:utf-8-*-


import unittest,time,HTMLTestRunner
from utils.sendmailatt import SendMail

def createSuite():
    suite = unittest.TestSuite()
    case_dir = './test/testCase/'
    discover = unittest.defaultTestLoader.discover(case_dir,pattern='*.py',top_level_dir=None)

    for test_suite in discover:
        for testcase in test_suite:
            suite.addTest(testcase)
            print(suite)
    return  suite

def run():
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/'+ now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'接口测试报告',
                                           description=u'凯京物流云')
    alltestname = createSuite()

    runner.run(alltestname)

    # 发送邮件
    sendMail = SendMail('./config/mailconfig.yaml')
    sendMail.send_mail()

if __name__ == '__main__':
   run()