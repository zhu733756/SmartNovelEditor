# -*- coding: utf-8 -*-
# @Time    : 2019/5/7 14:59
# @Author  : zhu733756
# @FileName: config.py
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "NovelEditorServer.NovelEditorServer.settings")

from django.conf import settings

BASE_DIR=os.path.dirname(settings.BASE_DIR)

DEFAULT_CUSTOM_FILE_BASE_DIR=os.path.join(BASE_DIR,"CustomFiles")
CUSTOM_FILE_BASE_DIR=os.path.join(BASE_DIR,"CustomFiles/customPath.txt")