#!/usr/bin/python
# -*- coding: UTF-8 -*-
from . import log
import smtplib
from email.mime.text import MIMEText
from email.header import Header
log = log.Log()
def mailTips(headContent,innerContent,receiversList=[]):
    # 第三方 SMTP 服务
    mail_host="smtp.qq.com"  #设置服务器
    mail_user='xxx@xxx'    #用户名
    mail_pass="xxx"   #口令

    sender = 'xxxx@xxx'
    if not receiversList:
        receiversList = ['xxxx@xxx']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    message = MIMEText(innerContent, 'plain', 'utf-8')
    message['From'] = Header(sender)
    message['To'] =  Header("相关", 'utf-8')

    subject = headContent
    message['Subject'] = Header(subject, 'utf-8')


    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(sender, receiversList, message.as_string())
        smtpObj.quit()
        log.info("邮件发送成功 用户:%s 内容:%s" % (",".join(receiversList).encode('utf-8'),innerContent))
        return True
    except smtplib.SMTPException as e:
        log.info("邮件发送失败 用户:%s 内容:%s 异常错误:%s" % (",".join(receiversList).encode('utf-8'),innerContent,str(e)))
        return False
if __name__ == '__main__':
    headContent = '卡券账户余额告警'
    innerContent = 'income where error'
    log.info("xxxxxxx")
    mailTips(headContent,innerContent)

