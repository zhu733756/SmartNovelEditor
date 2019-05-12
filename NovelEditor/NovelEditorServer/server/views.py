from django.shortcuts import render
from django.http import JsonResponse
from django_redis import cache
import json
from .tools import *
# Create your views here.

def save_tinymce_content_as_txt(request):
    '''存储tinymce content纯文本为txt格式'''
    current_tinymce_path=request.GET.get('path',None)
    bookname=request.GET.get('mode',None)
    title=request.GET.get('file',None)
    content=request.GET.get('content',None)
    #last stored path:get_tinymce_store_path
    tinymce_path=get_tinymce_store_path() if not current_tinymce_path else current_tinymce_path
    book_path=os.path.join(tinymce_path,bookname)
    if not os.path.exists(book_path):
        os.makedirs(book_path)
    codecs.open(os.path.join(book_path,"{}.html".format(title)),"w",encoding="utf8").write(content)
    return JsonResponse({"status":200,"res":"ok"})

def get_list_from_txt(request):
    '''获取书籍和章节列表'''
    path =request.GET.get("path",None)
    tinymce_path= path if path else get_tinymce_store_path()
    res=find_folder_and_file_tools(tinymce_path)
    if not res:
        return JsonResponse({'status':404,"res":'fail to parse the tinymce path'})
    return JsonResponse({'status':200,"res":json.dumps(res)})

def get_article_from_path(request):
    '''根据文章路径获取文章内容'''
    mode=request.GET.get("mode",None)
    file=request.GET.get("file",None)
    article_path=os.path.join(get_tinymce_store_path(),mode,file+".html")
    if not article_path or not os.path.exists(article_path):
        return JsonResponse({"status":404,"res":"path not exist"})
    content=codecs.open(article_path,"r",encoding="utf8").read()
    return JsonResponse({"status":200,'content':content})
