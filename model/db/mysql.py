#!/usr/bin/env python
#coding=utf-8
import os
import settings
import MySQLdb
import MySQLdb.cursors
class mysql:
    def __init__(self):
        dbFilePath = settings.DB_STRING
        dbConfig = dbFilePath.line.strip("\n").split("|")
        if len(dbConfig) != 5:
            raise Exception,'db string is error'
        host = dbConfig[0]
        port = dbConfig[1]
        user = dbConfig[2]
        passwd = dbConfig[3]
        db = dbConfig[4]
        self.conn = MySQLdb.connect(host, port,user, passwd,db,cursorclass = MySQLdb.cursors.DictCursor)
        self.cursor = self.conn.cursor()

    def fetchAll(self, sql,data=[]):
        result = None
        if self.cursor.execute(sql,data):
            result = self.cursor.fetchall()
        return result
    def fetchOne(self, sql,data=[]):
        result = None
        if self.cursor.execute(sql,data):
            result = self.cursor.fetchone()
        return result
    def getList(self,tableName,colums,condition,orders='',limits=''):
        sql = "SELECT "+colums+" FROM " + tableName + " WHERE 1=1"
        if  type(condition) == dict:
            for i in condition.keys():
                sql = sql + " AND "+i+"=?"
        else:
            sql = sql + condition
        if orders !='':
            sql = sql+' order by '+orders
        if limits != '':
            sql = sql+' limit '+limits
        return self.fetchAll(sql,condition.values())
    def getOne(self,tableName,colums,condition,orders='',limits=''):
        sql = "SELECT "+colums+" FROM " + tableName + " WHERE 1=1"
        if  type(condition) == dict:
            for i in condition.keys():
                sql = sql + " AND "+i+"=?"
        else:
            sql = sql + condition
        if orders !='':
            sql = sql+' order by '+orders
        if limits != '':
            sql = sql+' limit '+limits
        return self.fetchOne(sql,condition.values())
    def insert(self, tableName, data):
        sql = "INSERT INTO " + tableName + "("

        sql = sql + ','.join(data.keys())
        sql = sql + ") VALUES('"
        sql = sql + "','".join(data.values())
        sql = sql + "')"
        status = self.cursor.execute(sql)
        self.conn.commit()
        return status
    def delete(self, tableName, condition):
        sql = "DELETE FROM " + tableName + " WHERE 1=1"
        if  type(condition) == dict:
            for i in condition.keys():
                sql = sql + " AND "+i+"=?"
        else:
            sql = sql + condition
        status = self.cursor.execute(sql, condition.values())
        self.conn.commit()
        return status
    def update(self, tableName, data,condition):
        sql = "UPDATE " + tableName + " SET "
        #update data
        if  type(data) == dict:
            for i in data.keys():
                sql = sql + " AND "+i+"=?"
        else:
            sql = sql + data
            #condition
        sql = sql + " WHERE 1=1 "
        if  type(condition) == dict:
            for i in condition.keys():
                sql = sql + " AND "+i+"=?"
        else:
            sql = sql + condition
        status = self.cursor.execute(sql, data.values()+condition.values())
        self.conn.commit()
        return status
    def execute(self,sql):
        status = self.cursor.execute(sql)
        self.conn.commit()
        return status