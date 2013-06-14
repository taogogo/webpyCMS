#!/usr/bin/env python
#coding=utf-8
import os
#网站信息
WEB_URL='http://127.0.0.1:8080/'
WEB_TITLE='webpyCMS'
WEB_DESCRIPTION='webpyCMS is a fastest and smallest CMS'
TEMPLATE_THEME='default'
PER_PAGE_COUNT = 10

#账号相关
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD='tao'

#项目配置
DEFAULT_PATH='/index/index'
DEBUG_SWITCH=True
STATUS_LIST = {1:'发布',0:'草稿'}

#路径信息
ROOT_PATH=os.getcwd()+'/'
DATA_DIR_PATH=ROOT_PATH+'data/'
TMP_DIR_PATH=ROOT_PATH+'data/cache/'

#目录结构
UPLOAD_DIR='static/upload/'
TPL_DIR = 'templates'
ADMIN_TPL_DIR='admin'

#数据库信息
DB_TYPE='sqlite'
DB_STRING=DATA_DIR_PATH+'cms.db'
DB_TABEL_PREFIX='cms_'

