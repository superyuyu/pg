#!/usr/bin/python 
# -*- coding: utf-8 -*-
import os
import sys
import traceback
import socket

sys.path.append("../lib/")
from . import config

DEBUG = 1
TEST = 2
ONLINE = 3

ENV = 3


class BaseClass:
    def __init__(self):
        # 常量
        self.debug = DEBUG
        self.test = TEST
        self.online = ONLINE
        # 环境
        self.env = ENV
        self.envConf = config.Config("env.conf")
        ip = self.get_ip()
        if self.env == DEBUG or ip == '192.168.4.238':
            self.envConf = config.Config("env.debug.conf")
        elif self.env == TEST or ip == '192.168.4.210':
            self.envConf = config.Config("env.test.conf")
        return

    def get_ip(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
        finally:
            s.close()

        return ip


if __name__ == '__main__':
    b = BaseClass()
    print(b.get_ip())
