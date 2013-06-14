# -*- coding: utf-8 -*-
#!/usr/bin/env python
#coding=utf-8
import web,time
from action.base import base as baseAction
import model
class comment(baseAction):
    def __init__(self):
        if self.isLogin() != True:
            raise web.seeother('/')
        baseAction.__init__(self)
        settings = self.getSettings()
        self.assignTplDir(settings.ADMIN_TPL_DIR)
    def list(self):
        inputParams = self.getInput()
        page = int(inputParams['page']) if inputParams.has_key('page') else 1
        settings = self.getSettings()
        count = settings.PER_PAGE_COUNT
        offset= (page-1)*count if page > 0 else 0
        commentObj = model.comment()
        condition = {}
        listData = commentObj.getOne('COUNT(*) AS `total`',condition)
        totalCount = listData['total']
        commentList = commentObj.getList('*',condition,'id desc',str(offset)+','+str(count))
        cmsObj = model.cms()
        for k,v in enumerate(commentList):
            atl=cmsObj.getOne('name,id',{'id':v['cmsId']})
            commentList[k]['atl'] =atl

        self.assign('commentList',commentList)
        pageString = self.getPageStr(self.makeUrl('comment','list'),page,count,totalCount)
        self.assign('pageString',pageString)
        return self.display('commentList')
    def delete(self):
        inputParams = self.getInput()
        if not inputParams.has_key('id') :
            settings = self.getSettings()
            web.seeother(settings.WEB_URL)
        id=inputParams['id']
        condition={'id':str(id)}
        result=model.comment().delete(condition)
        if result:
            return self.success('删除成功',self.makeUrl('comment','list'))
        else:
            return self.error('删除失败')