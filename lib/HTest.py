#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import logging
import logging.handlers
import time
import conf
import requests
import json
import cookielib
import log
import traceback
log = log.Log()

class Http(object):

    def __init__(self):
        self.timeOutLimit = 10
        #userAget
        userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"
        referer = ""
        #cookies
        cookies = {}
        cookies["pfu"]="171816197"
        cookies["pfl"]="ZTkxY2Y5NTYxY2U3MjNhOGRjOTAwMmU0MmRmOWQ5NmUwY2VlYzk2ZmExYzI4MmYwMTY0M2VmMWM0ZGEyNjE0MSx4MzN0YmgzZXVhZjZ6endzN21lMzNoYTZiZTl6OHV4bSwxNTMyODc4MjIx"
        cookies["pfs"]="isvckeuwzchzB0ygQWmUSv01yng"
        cookies["pfp"]="3CImvpZ0tAD7kTNWla20hs8kbjhhPJkcddk94ene"
        cookies["pfe"]=str(int(time.time()))
        #header
        header = {}
        header["user-agent"] = userAgent
        header["Referer"] = referer
        #header["Cookie"] = cookies

        self.headers = header
        self.cookies = cookies
        pass



    def get(self,url,paramsDict=None):
        if not url:
            log.error("get fail. url is empty")
            return False
        try:
            log.info("url:%s params:%s" % (url,json.dumps(paramsDict)))
            if paramsDict:
                r = requests.get(url,timeout=self.timeOutLimit,params = paramsDict,headers=self.headers,cookies=self.cookies)
            else:
                r = requests.get(url,timeout=self.timeOutLimit,headers=self.headers,cookies=self.cookies)

            cookies = requests.utils.dict_from_cookiejar(r.cookies)
            #self.cookies = cookies
            print cookies
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
    url = 'https://www.jianshu.com/p/ca55407f9146'
    d = h.get(url)
    #print d
    print "end"
