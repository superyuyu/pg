#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import logging
import logging.handlers
import time
from . import config
from . import Base
class Log(Base.BaseClass):

    __instance=None

    def __new__(cls,*args,**kwd):
        if not cls.__instance:
            cls.__instance = super(Log, cls).__new__(cls, *args, **kwd)
        return cls.__instance

    def __init__(self):
        Base.BaseClass.__init__(self)
        logConf = self.envConf
        logpath = logConf.get("common.log_path")
        name = os.path.realpath(sys.argv[0]).split("/")[-1].split(".")[:-1][0]
        self.path = logpath
        rq = time.strftime('%Y%m%d',time.localtime(time.time()))#日期
        self.filename = name+'_' + rq + '.log'    # 日志文件名称 
        self.name = name
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(logging.INFO)
        self.fh = logging.FileHandler(self.path + self.filename)
        self.fh.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('%(asctime)s_%(name)s_func:%(funcName)s_line:%(lineno)s %(levelname)s: %(message)s')
        self.fh.setFormatter(self.formatter)
        if not self.logger.handlers:
            self.logger.addHandler(self.fh)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def debug(self, msg):
        self.logger.debug(msg)

    def close(self):
        self.logger.removeHandler(self.fh)



if __name__ == "__main__":
    log = Log()
    print(id(log))
    log.info("asdad")

