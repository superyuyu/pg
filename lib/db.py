#!/usr/bin/python          
# -*- coding: utf-8 -*- 
import os,sys
import MySQLdb as mdb
import MySQLdb.cursors
import conf
import Base

class Mysqldb(Base.BaseClass):
    def __init__(self,prefix):
        #cf = conf.Config("db.conf")
        Base.BaseClass.__init__(self)
        cf = self.envConf
        host,port,user,pwd,dbName = self.initDbConf(prefix,cf)
        if not host or not port or not user or not pwd or not dbName:
            return False 
        self.conn = mdb.connect(host,user,pwd,dbName,int(port),charset='utf8',cursorclass = MySQLdb.cursors.DictCursor)
        self.cur = self.conn.cursor()

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def select(self,sql):
        if not sql:
            return False
        total = self.cur.execute(sql)
        data = [row for row in self.cur.fetchall()]
        return data

    def executemany(self,sql,params):
        if not sql or not params:
            return False
        ret = self.cur.executemany(sql,params)
        self.conn.commit()
        return ret

    def execute(self,sql):
        if not sql:
            return False
        ret = self.cur.execute(sql)
        self.conn.commit()
        return ret

    
    def initDbConf(self,prefix,conf):
        if not prefix:
            prefix = "db" 
        host = conf.get("%s.db_host" % prefix)
        port = conf.get("%s.db_port" % prefix)
        user = conf.get("%s.db_user" % prefix)
        pwd = conf.get("%s.db_pwd" % prefix)
        dbName = conf.get("%s.db_name" % prefix)

        return host,port,user,pwd,dbName



if __name__ == "__main__":

    db = Mysqldb('db')

    data = db.select("select * from shopping_trade_info limit 10")
    id = data[0]["trans_id"]
    print id
    exit(1)

    conf = conf.Config("db.conf")
    host = conf.get("db_test.db_host")
    port = conf.get("db_test.db_port")
    user = conf.get("db_test.db_user")
    pwd = conf.get("db_test.db_pwd")
    dbName = conf.get("db_test.db_name")
    db = Mysqldb(host,port,user,pwd,dbName)
    data = db.select("select * from shopping_trade_info limit 10")
    id = data[0]["trans_id"]
    print id
    data = db.select("select *from shopping_trade_info where trans_id='%s'" % id)
    print data
