# -*- coding: utf-8 -*-
# @Time    : 2019/5/8 9:20
# @Author  : zhu733756
# @FileName: urls.py

from django.conf.urls import url
from .views import save_tinymce_content_as_txt,\
    get_list_from_txt,save_book_items,\
    get_article_from_path,search_biquge5200

urlpatterns = [
    url('^tinymce/store/$',save_tinymce_content_as_txt),
    url('^custom/books/infos/$',get_list_from_txt),
    url('^storage/books/infos/$',save_book_items),
    url('^custom/articles/$',get_article_from_path),
    url('^spiders/biquge5200/search/$',search_biquge5200),
]
