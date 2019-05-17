from django.http import JsonResponse
from .tools import *
from django.views.decorators.csrf import csrf_exempt
from .interfaces import BookInfoSpider
import sys


# Create your views here.

@csrf_exempt
def save_tinymce_content_as_txt(request):
    '''存储tinymce content纯文本为txt格式'''
    if request.method == "POST":
        bookInfos = json.loads(request.body.decode())
        current_tinymce_path = bookInfos.get('path', None)
        bookname = bookInfos.get('mode', None)
        title = bookInfos.get('file', None)
        content = bookInfos.get('content', "")
        # last stored path:get_tinymce_store_path
        tinymce_path = get_tinymce_store_path() if not current_tinymce_path else current_tinymce_path
        book_path = os.path.join(tinymce_path, bookname)
        if not os.path.exists(book_path):
            os.makedirs(book_path)
        codecs.open(os.path.join(book_path, "{}.html".format(title)), "w", encoding="utf8").write(content)
        return JsonResponse({"status": 200, "res": "ok"})


def get_list_from_txt(request):
    '''获取书籍和章节列表'''
    path = request.GET.get("path", None)
    tinymce_path = path if path else get_tinymce_store_path()
    res = find_folder_and_file_tools(tinymce_path)
    if not res:
        return JsonResponse({'status': 404, "res": 'fail to parse the tinymce path'})
    return JsonResponse({'status': 200, "res": json.dumps(res)})


def get_article_from_path(request):
    '''根据文章路径获取文章内容'''
    mode = request.GET.get("mode", None)
    file = request.GET.get("file", None)
    article_path = os.path.join(get_tinymce_store_path(), mode, file + ".html")
    if not article_path or not os.path.exists(article_path):
        return JsonResponse({"status": 404, "res": "path not exist"})
    content = codecs.open(article_path, "r", encoding="utf8").read()
    return JsonResponse({"status": 200, 'content': content})


@csrf_exempt
def save_book_items(request):
    '''处理前端发送的bookItems，存储对应的文件路径或者文件夹'''
    if request.method == "POST":
        bookItems = json.loads(request.body.decode())["bookItems"]
        if not bookItems:
            return JsonResponse({"status": 404, "res": "bookItems not get"})
        # 转移bookItems为文件夹路径
        try:
            bookItems_differece, local_filepath = transfer_bookItems_to_filepaths(bookItems)
            # 创建空文件夹
            if bookItems_differece:
                create_files(bookItems_differece)
            # 删除文件夹
            if local_filepath:
                remove_files(local_filepath)
            return JsonResponse({"status": 200})
        except Exception as e:
            return JsonResponse({"status": 500, "res": e.args})


def search_biquge5200(requst):
    '''通过笔趣阁5200获取搜索结果'''
    search_key = requst.GET.get("searchKey", None)
    if not search_key:
        return JsonResponse({"status": 404, "res": "cannot find a search key"})
    if "；" in search_key:
        search_key = search_key.replace("；", ";")
    searchKey = []
    searchKeyDict ={}
    if ";" not in search_key:
        searchKey.append(search_key)
    else:
        eachSearchKey = search_key.split(";")
        for key in eachSearchKey:
            key = key.replace("：", ":").strip()
            if ":" in key:
                author, book = key.split(":")
                searchKeyDict.append({author:book})
            else:
                searchKey.append(key)
    res = BookInfoSpider().split_key(*searchKey,**searchKeyDict)
    if not res:
        return JsonResponse({"status": 404, "res": "Cannot find the source on {}"
                            .format(sys._getframe().f_code.co_name)})
    return JsonResponse({"status": 200, "res": res})
