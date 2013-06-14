# -*- coding: utf-8 -*-
#!/usr/bin/env python
import web, time,math
import settings
class base:
    tplData = {}
    globalsTplFuncs = {}
    tplDir = ''
    referer = ''
    settings = {}
    errorMessage = ''
    def __init__(self):
        self.settings = settings
        self.tplData = {
            'webTitle' : self.settings.WEB_TITLE,
            'webUrl' : self.settings.WEB_URL,
            'webDescription' : self.settings.WEB_DESCRIPTION,
            'statusList':self.settings.STATUS_LIST
        }
        self.globalsTplFuncs = {}
        self.tplDir = ''
        self.initCommonTplFunc()
        self.referer= web.ctx.env.get('HTTP_REFERER', self.settings.WEB_URL)

    #初始化模板内置函数
    def initCommonTplFunc(self):
        subStr=lambda strings,offset,length : self.subText(strings,offset,length)
        makeUrl= lambda action,method='index',params={} : self.makeUrl(action,method,params)
        self.assignTplFunc({'subStr':subStr,'makeUrl':makeUrl})

    #截断去除html标记后的字符串
    def subText(self,strings,offset,length):
        return self.strip_tags(strings)[offset:length]

    #去除html标记
    def strip_tags(self,html):
        from HTMLParser import HTMLParser
        html=html.strip()
        html=html.strip("\n")
        result=[]
        parse=HTMLParser()
        parse.handle_data=result.append
        parse.feed(html)
        parse.close()
        return "".join(result)

    #注册变量
    def assign(self,key,value=''):
        if type(key) == dict:
            self.tplData = dict(self.tplData,**key)
        else:
            self.tplData[key] = value

    #显示模板
    def display(self,tplName):
        if self.tplDir == '':
            self.assignTplDir(settings.TEMPLATE_THEME)
        print self.tplDir,settings.TEMPLATE_THEME
        self.tplData['render'] = web.template.render(self.tplDir,globals=self.globalsTplFuncs)
        return getattr(self.tplData['render'], tplName)(self.tplData)

    #注册模板目录
    def assignTplDir(self,tplDir):
        self.tplDir = settings.TPL_DIR+'/'+tplDir+'/'

    #注册模板函数
    def assignTplFunc(self,funcs):
        self.globalsTplFuncs = dict(self.globalsTplFuncs,**funcs)

    #成功提示
    def success(self,msg,url,timeout=5):
        tplData = {'msg': msg, 'url': url,'timeout':timeout}
        self.assign('jump',tplData)
        return self.display('success')

    #错误提示
    def error(self,msg,url=None,timeout=5):
        if url ==None:
            url= web.ctx.env.get('HTTP_REFERER', self.settings.WEB_URL)
        tplData={'msg':msg,'url':url,'timeout':timeout}
        self.assign('jump',tplData)
        return self.display('error')

    #生成url
    def makeUrl(self,action,method='index',params={}):
        import urllib
        paramsStr = '?'+urllib.urlencode(params) if len(params)>0 else ''
        return self.settings.WEB_URL+action+'/'+method+paramsStr

    #是否已经登陆
    def isLogin(self):
        return hasattr(web.ctx.session, 'login') and web.ctx.session.login == True

    #设置登陆变量
    def setLogin(self,userData=None):
        if userData == None:
            web.ctx.session.login = False
        else:
            web.ctx.session.login = True
            web.ctx.session.username = userData['username']

    #销毁session
    def sessionDestroy(self):
        web.ctx.session.kill()

    def getInput(self):
        #return web.input()
        return self.htmlquote(dict(web.input()))
    def htmlquote(self,inputData):
        if isinstance(inputData,dict) == False:
            return web.net.htmlquote(inputData)
        else:
            for k,v in inputData.items():
                inputData[k]= self.htmlquote(v)
        return inputData
    def htmlunquote(self,inputData):
        if isinstance(inputData,dict) == False:
            return web.net.htmlunquote(inputData)
        else:
            for k,v in inputData.items():
                inputData[k]= self.htmlunquote(v)
        return inputData
    def getPageStr(self,url,currentPage,perPageCount,totalCount=10000):
        totalPage = int(math.ceil(totalCount/perPageCount))
        if '?' in url:
            url=url+'&page='
        else:
            url=url+'?page='
        pageString= ''

        if currentPage > 1:
            pageString += '''
                <span class="alignleft"><a href="'''+url+str(currentPage-1)+'''">&laquo; 上一页</a></span>
            '''
        if totalPage>currentPage:
            pageString = pageString+'''
            <span class="alignright"><a href="'''+url+str(currentPage+1)+'''">下一页 &raquo;</a></span>
        '''
        return pageString
    def getSettings(self):
        return self.settings
    def validates(self,validList):
        userInput=self.getInput()
        for i in validList:
            if not i.validate(userInput[i.name]):
                self.errorMessage=i.note
                return False
        return True
