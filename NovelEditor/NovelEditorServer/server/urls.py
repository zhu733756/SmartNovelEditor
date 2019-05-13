# -*- coding: utf-8 -*-
# @Time    : 2019/5/8 9:20
# @Author  : zhu733756
# @FileName: urls.py

from django.conf.urls import url
from .views import *

urlpatterns = [
    url('^tinymce/store/$',save_tinymce_content_as_txt),
    url('^custom/books/infos/$',get_list_from_txt),
    url('^storage/books/infos/$',save_book_items),
    url('^custom/articles/$',get_article_from_path),
]
