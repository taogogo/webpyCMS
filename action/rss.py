# -*- coding: utf-8 -*-
#coding=utf-8
import web,time,settings
from action.base import base as baseAction
import model
class rss(baseAction):
    def __init__(self):
        baseAction.__init__(self)
        settings = self.getSettings()
        self.assignTplDir(settings.ADMIN_TPL_DIR)
    def index(self):
        cmsList = model.cms().getList('*',{},'id desc')
        self.assign('cmsList',cmsList)
        return self.display('rss')