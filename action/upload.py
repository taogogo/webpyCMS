# -*- coding: utf-8 -*-
#!/usr/bin/env python
#coding=utf-8
import web,time
from action.base import base as baseAction
import model
class upload(baseAction):
    def __init__(self):
        if self.isLogin() != True:
            raise web.seeother('/')
        baseAction.__init__(self)
        settings = self.getSettings()
        self.assignTplDir(settings.ADMIN_TPL_DIR)
    def index(self):
        return self.display('uploadFile')
    def upload(self):
        inputParams = web.input(uploadFile={})
        settings = self.getSettings()
        filedir = settings.ROOT_PATH+settings.UPLOAD_DIR # change this to the directory you want to store the file in.
        if 'uploadFile' in inputParams: # to check if the file-object is created
            filepath=inputParams.uploadFile.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.
            filename=filepath.split('/')[-1] # splits the and chooses the last part (the filename with extension)
            fout = open(filedir +'/'+ filename,'w') # creates the file where the uploaded file should be stored
            fout.write(inputParams.uploadFile.file.read()) # writes the uploaded file to the newly created file.
            fout.close() # closes the file, upload complete.
        self.assign('text',settings.WEB_URL+settings.UPLOAD_DIR+filename)
        return self.display('copyText')