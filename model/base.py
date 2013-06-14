# -*- coding: utf-8 -*-
#!/usr/bin/env python
#coding=utf-8
from model.db.database import *
class base:
    def getTable(self):
        return self.__class__.__name__

    def getDb(self):
        return database()

    def insert(self,data):
        return self.getDb().insert(self.getTable(),data)

    def delete(self,condition):
        return self.getDb().delete(self.getTable(), condition)

    def getList(self,colums,condition,orders='',limits=''):
        return self.getDb().getList(self.getTable(),colums,condition,orders,limits)

    def getOne(self,colums,condition,orders='',limits=''):
        return self.getDb().getOne(self.getTable(),colums,condition,orders,limits)

    def update(self, data,condition):
        return self.getDb().update(self.getTable(),data,condition)
