#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys 
import json
import urllib
from . import log
from . import Base
from . import http
log = log.Log()
def sendSms(msisdn,msg):
    if not msisdn or not msg:
        log.info("msisdn or msg has empty msisdn:%s msg:%s" % (msisdn,msg))
        return False
    #获取请求地址
    base = Base.BaseClass()
    baseUrl = base.envConf.get("common.sms_url") 
    method = "/notify/sms"
    msg = msg.replace("&","")
    smsData = {}
    smsData["countrycode"] = ""
    smsData["msisdn"] = msisdn
    smsData["msg"] = urllib.quote(msg)
    url = "%s%s" % (baseUrl,method)
    h = http.Http() 
    ret = h.post(url,smsData)
    if ret:
        ret = json.loads(ret.encode("utf-8"))
        if ret["status"] == 200:
            log.info("短信发送成功 msisdn:%s msg:%s" % (msisdn.encode('utf-8'),msg))
            return True 
    log.info("短信发送失败 msisdn:%s msg:%s" % (msisdn.encode('utf-8'),msg))
    return False
    
if __name__ == '__main__':
    sendSms("8618612307535",'aaa')
    pass
