#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import logging
import logging.handlers
import time
import requests
import json
import traceback
from . import log
log = log.Log()

class Http(object):

    def __init__(self):
        cookies = {}
        cookies['UID'] = '16F72a24619110367ed665c1523413673'
        cookies['UIDR'] = '1523413673'
        self.timeOutLimit = 10
        self.cookies = cookies
        self.headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
        pass

    def get(self,url,paramsDict=None):
        if not url:
            log.error("get fail. url is empty")
            return False
        try:
            log.info("url:%s params:%s" % (url,json.dumps(paramsDict)))
            if paramsDict:
                r = requests.get(url, params = paramsDict)
            else:
                r = requests.get(url,headers = self.headers)

            log.info("get ret:%s url:%s params:%s" % (r.text,url,json.dumps(paramsDict)))
            if r.headers['Content-Type'].find('application/json')!=-1 or r.headers['content-type'].find('application/json')!=-1:
                return r.json()
            else:
                return r.text

        except Exception as e:
            log.error("Http get Exception:%s" % (traceback.format_exc()))
            return False
        return True

    def post(self,url,paramsDict=None):
        if not url:
            log.error("post fail. url is empty")
            return False
        try:
            log.info("url:%s params:%s" % (url,json.dumps(paramsDict)))
            if paramsDict:
                r = requests.post(url,timeout=self.timeOutLimit,data = paramsDict)
            else:
                r = requests.post(url,timeout=self.timeOutLimit)

            log.info("post ret:%s url:%s params:%s" % (r.text,url,json.dumps(paramsDict)))
            if r.headers['Content-Type'].find('application/json')!=-1 or r.headers['content-type'].find('application/json')!=-1:
                return r.json()
            else:
                return r.text

        except Exception as e:
            log.error("Http post Exception:%s" % (traceback.format_exc()))
            return False
        return True

        pass

if __name__ == "__main__":
    h = Http()
    url = 'https://docs.qq.com/dop-api/opendoc?id=DWWdkS1VSZHFWWmxn&outformat=1&normal=1&startrow=0&endrow=60&wb=1&nowb=0&t=1598863832579'
    d = h.get(url)
    print(d)

