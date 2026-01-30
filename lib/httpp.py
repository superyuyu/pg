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
import random
from . import log

log = log.Log()


class Http(object):

    def __init__(self, cookies=None):
        if cookies:
            self.cookies = cookies
        else:
            cookies = {}
            cookies['UID'] = '16F72a24619110367ed665c1523413673'
            cookies['UIDR'] = '1523413673'
            self.cookies = cookies
        self.timeOutLimit = 10
        self.headers = {
            'User-Agent': self._generate_random_user_agent()}
        pass
    
    def _generate_random_user_agent(self):
        platforms = ['Windows NT 10.0', 'Windows NT 6.1', 'Windows NT 6.3', 'Macintosh; Intel Mac OS X 10_15_7', 'Macintosh; Intel Mac OS X 10_14_6', 'X11; Linux x86_64']
        browsers = [
            ('Chrome', '91.0.4472.124', 'AppleWebKit/537.36', 'KHTML, like Gecko', 'Safari/537.36'),
            ('Firefox', '89.0', 'Gecko/20100101'),
            ('Safari', '14.1.1', 'AppleWebKit/605.1.15', 'KHTML, like Gecko')
        ]
        
        platform = random.choice(platforms)
        browser_info = random.choice(browsers)
        
        if browser_info[0] == 'Chrome':
            return f'Mozilla/5.0 ({platform}) {browser_info[2]} ({browser_info[3]}) {browser_info[0]}/{browser_info[1]} {browser_info[4]}'
        elif browser_info[0] == 'Firefox':
            return f'Mozilla/5.0 ({platform}; rv:{browser_info[1]}) {browser_info[2]} {browser_info[0]}/{browser_info[1]}'
        else:  # Safari
            return f'Mozilla/5.0 ({platform}) {browser_info[2]} ({browser_info[3]}) Version/{browser_info[1]} {browser_info[0]}/{browser_info[1]}'

    def get(self, url, paramsDict=None):
        if not url:
            log.error("get fail. url is empty")
            return False
        try:
            log.info("get url:%s params:%s" % (url, json.dumps(paramsDict)))
            if paramsDict:
                r = requests.get(url, headers=self.headers, cookies=self.cookies, timeout=self.timeOutLimit, params=paramsDict)
            else:
                r = requests.get(url, headers=self.headers, cookies=self.cookies, timeout=self.timeOutLimit)

            #log.info("get ret:%s url:%s params:%s" % (r.text, url, json.dumps(paramsDict)))
            if r.headers['Content-Type'].find('application/json') != -1 or r.headers['content-type'].find(
                    'application/json') != -1:
                return r.json()
            else:
                return r.text

        except Exception as e:
            log.error("Http get Exception:%s" % (traceback.format_exc()))
            return False
        return True

    def post(self, url, paramsDict=None):
        if not url:
            log.error("post fail. url is empty")
            return False
        try:
            log.info("post url:%s params:%s" % (url, json.dumps(paramsDict)))
            if paramsDict:
                r = requests.post(url, headers=self.headers, cookies=self.cookies, timeout=self.timeOutLimit, data=paramsDict)
            else:
                r = requests.post(url, headers=self.headers, cookies=self.cookies, timeout=self.timeOutLimit)

            #log.info("post ret:%s url:%s params:%s" % (r.text, url, json.dumps(paramsDict)))
            if r.headers['Content-Type'].find('application/json') != -1 or r.headers['content-type'].find(
                    'application/json') != -1:
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
