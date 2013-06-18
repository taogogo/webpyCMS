# -*- coding: utf-8 -*-
#!/usr/bin/env python
import web, time

import settings
from model.base import base as BaseModel
from utils.function import *
@singleton
class cms(BaseModel):
    def __init__(self):
        pass