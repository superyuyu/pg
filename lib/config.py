#!/usr/bin/python          
#-*- coding: utf-8 -*-
import os,sys
import configparser

class Config:
    def __init__(self,fileName=None):
        self.conf = configparser.ConfigParser()
        currentDir = os.path.dirname(os.path.abspath(__file__))
        confFile = os.path.join(currentDir+'/../config/',fileName)
        self.conf.read(confFile)

    #获取配置 结构为:section.key
    def get(self,inputStr):
        inputList = inputStr.split('.')
        if len(inputList) != 2:
            return None
        return self.conf.get(inputList[0],inputList[1])



