import os
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config.config import CONFIG_PATH

# 获取到测试报个的路径
DATA_PATH = os.path.join(CONFIG_PATH, 'reports')


class SendMail:
    """发送邮件"""

    def __init__(self, mail_host="smtp.qq.com", mail_user="386160165@qq.com", mail_pass="bffglivubozabgie",
                 sender='386160165@qq.com'):
        self.mail_host = mail_host  # 设置服务器
        self.mail_user = mail_user  # 用户名
        self.mail_pass = mail_pass  # 口令
        self.sender = sender  # 发件人
        self.message = MIMEMultipart()
        self.receivers = ['386160165@qq.com', '923483629@qq.com', '1563374406@qq.com', '455736491@qq.com',
                          '1058741880@qq.com', '736174519@qq.com', '876040548@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
        self.DATA_PATH1 = os.path.join(DATA_PATH, self.file_name())

    def read_report(self):
        """读取测试报告"""
        file = open(self.DATA_PATH1, 'rb').read()
        return file

    def file_name(self, folder=DATA_PATH):
        """获取到最新的测试报告"""
        files = ''
        for root, dirs, files in os.walk(folder):
            files = files[-1]
        return files

    def send_mail(self, body='详情查看测试报告请请下载附件，预览查看显示效果会有差别'):
        att1 = MIMEText(self.read_report(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename是附件的名字
        att1["Content-Disposition"] = 'attachment; filename="{}"'.format(self.file_name())
        self.message.attach(att1)

        self.message['From'] = Header("386160165@qq.com", 'utf-8')
        self.message['To'] = Header(str(self.receivers), 'utf-8')
        subject = 'web自动化测试报告'
        self.message['Subject'] = Header(subject, 'utf-8')
        # 邮件正文内容
        self.message.attach(MIMEText(body, 'plain', 'utf-8'))

        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.mail_host, 25)  # 25 为 SMTP 端口号
            smtpObj.login(self.mail_user, self.mail_pass)
            smtpObj.sendmail(self.sender, self.receivers, self.message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")


# SendMail().send_mail()

class SendMail2:
    """发送邮件"""

    def __init__(self, mail_host="smtp.qq.com", mail_user="386160165@qq.com", mail_pass="bffglivubozabgie",
                 sender='386160165@qq.com'):
        self.mail_host = mail_host  # 设置服务器
        self.mail_user = mail_user  # 用户名
        self.mail_pass = mail_pass  # 口令
        self.sender = sender  # 发件人
        self.message = MIMEMultipart()
        self.receivers = ['386160165@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
        self.DATA_PATH1 = os.path.join(DATA_PATH, self.file_name())

    def read_report(self):
        """读取测试报告"""
        file = open(self.DATA_PATH1, 'rb').read()
        return file

    def file_name(self, folder=DATA_PATH):
        """获取到最新的测试报告"""
        files = ''
        for root, dirs, files in os.walk(folder):
            files = files[-1]
        return files

    def send_mail(self, body='详情查看测试报告请请下载附件，预览查看显示效果会有差别'):
        att1 = MIMEText(self.read_report(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename是附件的名字
        att1["Content-Disposition"] = 'attachment; filename="{}"'.format(self.file_name())
        self.message.attach(att1)

        self.message['From'] = Header("386160165@qq.com", 'utf-8')
        self.message['To'] = Header(str(self.receivers), 'utf-8')
        subject = 'web自动化测试报告'
        self.message['Subject'] = Header(subject, 'utf-8')
        # 邮件正文内容
        self.message.attach(MIMEText(body, 'plain', 'utf-8'))

        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.mail_host, 25)  # 25 为 SMTP 端口号
            smtpObj.login(self.mail_user, self.mail_pass)
            smtpObj.sendmail(self.sender, self.receivers, self.message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")


SendMail2().send_mail()