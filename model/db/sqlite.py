#!/usr/bin/env python
#coding=utf-8
import sqlite3 as db
import os
import settings

class sqlite:
    def __init__(self):
        dbFilePath = settings.DB_STRING
        if os.path.exists(dbFilePath):
            #如果数据库存在，就直接连接
            self.conn = db.connect(dbFilePath)
            self.cursor = self.conn.cursor()
        else:
            raise Exception,'db not exists'

    def fetchAll(self, sql,data=[]):
        result = None
        #print sql,data
        if self.cursor.execute(sql,data):
            result = self.cursor.fetchall()
            if len(result) > 0:
                return [dict(zip([j[0] for j in self.cursor.description], i)) for i in result]
        return result

    def fetchOne(self, sql,data=[]):
        result = None
        if self.cursor.execute(sql,data):
            result = self.cursor.fetchone()
            #print dict(zip([j[0] for j in self.cursor.description],result))
            if result != None:
                return dict(zip([j[0] for j in self.cursor.description], result))
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
        result = self.fetchAll(sql,condition.values())
        result = [] if result == None else result
        return result
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
        sql = "INSERT INTO " + tableName + " ("+','.join(data.keys())+") VALUES ("+("?,"*len(data))[:-1]+")"
        print sql
        status = self.cursor.execute(sql, data.values())
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
        sql = "UPDATE " + tableName + " SET  "
        #update data
        if  type(data) == dict:
            for i in data.keys():
                sql = sql + " "+i+"=?,"
        else:
            sql = sql + data
            #condition
        sql = sql[:-1] + " WHERE 1=1 "
        if  type(condition) == dict:
            for i in condition.keys():
                sql = sql + " AND "+i+"=?"
        else:
            sql = sql + condition
        status = self.cursor.execute(sql, data.values()+condition.values())
        self.conn.commit()
        return status
    def execute(self,sql,data=[]):
        print sql
        status = self.cursor.execute(sql,data=[])
        self.conn.commit()
        return status