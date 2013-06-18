# -*- coding: utf-8 -*-
#!/usr/bin/env python
#coding=utf-8
import web,time
from action.base import base as baseAction
import model
class index(baseAction):
    def __init__(self):
        baseAction.__init__(self)
        settings = self.getSettings()
        self.assignTplDir(settings.TEMPLATE_THEME)
    def index(self):
        settings = self.getSettings()
        count = settings.PER_PAGE_COUNT
        inputParams = self.getInput()
        page = int(inputParams['page']) if inputParams.has_key('page') else 1
        offset= (page-1)*count if page > 0 else 0
        cmsObj = model.cms()
        condition = {'status':1}
        listData = cmsObj.getOne('COUNT(*) AS `total`',condition)
        totalCount = listData['total']
        cmsList = cmsObj.getList('*',condition,'orders desc,createTime desc',str(offset)+','+str(count))
        self.assign('cmsList',cmsList)
        pageString = self.getPageStr(self.makeUrl('index','index'),page,count,totalCount)
        self.assign('pageString',pageString)
        commentObj=model.comment()
        commentList = commentObj.getList('*',{'status':1},'id desc',str(offset)+','+str(count))
        self.assign('commentList',commentList)

        return self.display('index')

    def show(self):
        inputParams = self.getInput()
        if not inputParams.has_key('id') :
            settings = self.getSettings()
            web.seeother(settings.WEB_URL)
        id=inputParams['id']
        cmsObj = model.cms()
        condition = {'status':1,'id':str(id)}
        atl = cmsObj.getOne('*',condition)
        if atl == None:
            raise web.notfound('not found')
        atl['views']+=1
        updateData = {'views':(atl['views'])}
        #view count incr
        cmsObj.update(updateData,condition)
        commentList=model.comment().getList('*',{'status':1,'cmsId':int(id)})
        self.assign('atl',atl)
        self.assign('commentList',commentList)
        return self.display('show')
    def comment(self):
        userInput= self.getInput()
        cmsObj = model.cms()
        cmsId = userInput['cmsId']
        condition = {'status':1,'id':cmsId}
        atl = cmsObj.getOne('*',condition)
        if atl == None:
            return self.error('文章不存在')
        from web import form
        validList=(
            form.Textbox("name",form.regexp(r".{3,100}$", '姓名需为3~100个字符')),
            form.Textbox("content",form.regexp(r".{1,100}$", '评论内容需为3~100个字符')),
            form.Textbox("email", form.regexp(r".*@.*", '邮箱格式错误')),
            form.Textbox("email",form.regexp(r".{5,100}$", '邮箱需为5~100个字符')),
            )
        if not self.validates(validList):
            return self.error(self.errorMessage)
        date = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        ip=web.ctx.ip
        data={
            'cmsId':cmsId,
            'content':userInput['content'],
            'name':userInput['name'],
            'email':userInput['email'],
            'createTime':date,
            'ip':ip,
            'status':1
        }
        model.comment().insert(data)
        data = {'commentCount':atl['commentCount']+1}
        model.cms().update(data,condition)
        return self.success('评论成功',self.referer)
