#!/usr/bin/env python
#coding=utf-8
import web, settings

urls = (
    '([a-z0-9\/]*)', 'dispatcher'
    )

class dispatcher:
    def __init__(self):
        pass
    def GET(self, path):
        return self.__request(path)

    def POST(self, path):
        return self.__request(path)

    def __request(self, path=''):
        try:
            if path.count('/') < 2:
                path = settings.DEFAULT_PATH
            modelName, controllerName = path.strip()[1:].split('/', 1)
            if not controllerName:
                controllerName = 'index'
            if not modelName or not controllerName:
                return 'model/controller missing'
            moduleList = __import__('action.' + modelName, {}, {}, [modelName])
            modelObj = getattr(moduleList, modelName)()
            if hasattr(modelObj, controllerName):
                result = getattr(modelObj, controllerName)()
            else:
                result = 'no controller'
            return result
        except Exception ,e:
            from action.base import base as baseAction
            baseObj=baseAction()
            if e.message == 'db not exists' :
                return baseObj.error('尚未安装',baseObj.makeUrl('install'))
            return baseObj.error(e.message,baseObj.makeUrl('index'))
            #raise Exception,e.message
def session_hook():
    web.ctx.session = session

if __name__ == "__main__":
    app = web.application(urls, globals())
    #web.header("Content-Type","text/html; charset=utf-8")
    web.config.session_parameters['cookie_name'] = 'py_wpcms_sid'
    web.config.session_parameters['cookie_domain'] = None
    web.config.session_parameters['timeout'] = 86400,
    web.config.session_parameters['ignore_expiry'] = True
    web.config.session_parameters['ignore_change_ip'] = True
    web.config.session_parameters['secret_key'] = 'JJIEhi323rioes34hafwaj2'
    web.config.session_parameters['expired_message'] = 'Session expired'
    session = web.session.Session(app, web.session.DiskStore('data/sessions'), initializer={'login': False})
    def session_hook():
        web.ctx.session = session
    app.add_processor(web.loadhook(session_hook))
    app.run()