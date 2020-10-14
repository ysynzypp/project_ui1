# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/6 10:54
# @Author  : mao
# @Explain : 通过sql语句，读取数据库查询内容，以字典的形式输出
import pymysql
from common.ReadConfig import Config
import pprint
from common.log import logger
from Base.BasePath import path
class myqsldb:
    def __init__(self,host,port,user,passwd,dbname = None):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.dbname = dbname
    def dbconn(self):
        self.conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.passwd,
            db=self.dbname,
            charset='utf8')
        cursor = self.conn.cursor()
        return cursor

    def sqlquery(self,sqlcondition):
        self.cursor = self.dbconn()
        self.cursor.execute(sqlcondition)
        desc = self.cursor.description
        data_dict = [dict(zip([col[0] for col in desc], row)) for row in self.cursor.fetchall()] #将输入数据库读取到的内容转化为字典的格式输出
        self.conn.commit()
        logger.info(data_dict)
        return data_dict
    def close(self):
        self.cursor.close()
        self.conn.close()
class projectdb():
    def __init__(self,dbname = None,host = None,port =None,user =None,passwd = None,envdb = None):
        envdb = 'testdb' if envdb is None else envdb
        datafile = Config(path.MysqlConfig)
        host = datafile.get(envdb)['host'] if host is None else host
        port = datafile.get(envdb)['port'] if port is None else port
        user = datafile.get(envdb)['user'] if user is None else user
        passwd = datafile.get(envdb)['passwd'] if passwd is None else passwd
        self.pjdbcon = myqsldb(host=host, port=port, user=user, passwd=passwd, dbname=dbname)
    def pj_sql(self,sql):
        pjsqldata = self.pjdbcon.sqlquery(sql)
        return pjsqldata

if __name__ == "__main__":
    a = projectdb
    #b =a().pj_sql("SELECT te.* FROM  crm.team  t left join crm.team_members  te on t.team_id = te.team_id where  t.name = '刘代念团队' ")
    print(type(a))
    #pprint.pprint(b)
