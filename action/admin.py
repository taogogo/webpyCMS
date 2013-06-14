# -*- coding: utf-8 -*-
#!/usr/bin/env python
import web,time
from action.base import base as baseAction

class admin(baseAction):
    def __init__(self):
        baseAction.__init__(self)
        settings = self.getSettings()
        self.assignTplDir(settings.ADMIN_TPL_DIR)
    def check(self):
        from web import form
        validList=(
            form.Textbox("username",form.regexp(r".{3,20}$", '用户名为3~20个字符')),
            form.Password("password", form.regexp(r".{3,20}$", '密码为3~20个字符')),
        )
        if not self.validates(validList):
            return self.error(self.errorMessage)
        inputData = self.getInput()
        settings = self.getSettings()
        if settings.ADMIN_USERNAME == inputData['username'] and settings.ADMIN_PASSWORD == inputData['password']:
            userData={'username':inputData['username']}
            self.setLogin(userData)
            return self.success('登陆成功',self.makeUrl('cms','list'))
        else:
            return self.error('账号或密码错误',self.makeUrl('admin',''))

    def index(self):
        serverInfo = {
            'clientIp': web.ctx.ip,
            'date': str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())),
            'ua': web.ctx.environ['HTTP_USER_AGENT'],
            'serverIp': web.ctx.environ['REMOTE_ADDR']
        }
        self.assign('info',serverInfo)
        if self.isLogin():
            return self.display('index')
        else:
            return self.display('login')

    def logout(self):
        self.setLogin()
        return self.success('退出成功',self.makeUrl('index'))