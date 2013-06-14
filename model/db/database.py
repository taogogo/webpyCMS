#!/usr/bin/env python
#coding=utf-8
import sqlite3 as db
import os
import settings
class database :
    dbObj = None
    #先验证数据库是否存在
    def __init__(self):
        modelName=settings.DB_TYPE
        if os.path.exists(settings.ROOT_PATH+'model/db/'+modelName+'.py') == False:
            raise Exception,'db class file not exists'
        dbList = __import__('model.db.'+modelName,{},{},modelName)
        if hasattr(dbList, modelName):
            modelObj = getattr(dbList, modelName)()
        else:
            raise Exception,'db class not exists'
        self.dbObj=modelObj

    def fetchAll(self,sql):
        return self.dbObj.fetchAll(sql)

    def fetchOne(self,sql):
        return self.dbObj.fetchOne(sql)

    def insert(self,tableName, data):
        return self.dbObj.insert(tableName,data)

    def delete(self, tableName, condition):
        return self.dbObj.delete(tableName,condition)

    def update(self, tableName, data,condition):
        return self.dbObj.update(tableName,data,condition)

    def execute(self,sql):
        print sql
        return self.dbObj.execute(sql)

    def getList(self,tableName,colums,condition,orders='',limits=''):
        return self.dbObj.getList(tableName,colums,condition,orders,limits)

    def getOne(self,tableName,colums,condition,orders='',limits=''):
        return self.dbObj.getOne(tableName,colums,condition,orders,limits)
