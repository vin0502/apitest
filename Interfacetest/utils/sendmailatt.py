#__author__ = 'pan'
# -*- coding:utf-8 -*-

import os,time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from utils.log import Log
from utils.readyaml import ReadYaml

#测试报告路径
reportPath = path = os.path.dirname(os.path.dirname(__file__)) + '/report/'
logger = Log()

class SendMail:
    '''定义发送带附件邮件'''

    def __init__(self, mail_config_file):
        config = ReadYaml(mail_config_file).getValue()
        self.sendTo = config['to_address']
        self.sender_name = config['sender_name']
        self.sender_pswd = config['sender_pswd']
        self.host = config['host']
        self.subject = config['subject']

    def __get_report(self):
        '''获得最新测试报告'''
        #获取目录下的所有文件
        lists = os.listdir(reportPath)
        lists.sort()
        new_report_name = lists[-1]
        print('The new report name: {0}'.format(new_report_name))
        return new_report_name

    def __messages(self):
        '''生成邮件内容,和html报告附件'''
        # 创建一个带附件的实例
        self.msg = MIMEMultipart()

        #生成邮件内容
        # 定义标题
        self.msg['Subject'] = self.subject
        # 定义发送时间
        self.msg['date'] = time.strftime('%a, %d %b %Y%H:%M:%S %z')
        # 定义正文
        new_report = self.__get_report()
        f = open(os.path.join(reportPath, new_report), 'rb')
        mail_body = f.read()
        f.close()
        html =  MIMEText(mail_body, _subtype='html', _charset='utf-8')
        self.msg.attach(html)


        # 构造html附件
        att = MIMEText(mail_body, 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename= "TestReport.html"'#这里的filename可以任意写，写什么名字，邮件中显示什么名字
        self.msg.attach(att)

    def send_mail(self):
        '''
        sub:主题
        content:内容
        send_mail("aaa@126.com","sub","content")
        '''
        self.__messages()
        self.msg['mail_from'] = self.sender_name
        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.host)
            smtp.login(self.sender_name, self.sender_pswd)
            smtp.sendmail(self.msg['mail_from'], self.sendTo, self.msg.as_string())
            smtp.quit()
            logger.info("邮件发送成功")
        except Exception:
            logger.error("邮件发送失败")
            raise

if __name__ == '__main__':
    sendMail = SendMail('../config/mailconfig.yaml')
    sendMail.send_mail()






