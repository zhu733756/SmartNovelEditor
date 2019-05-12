# -*- coding: utf-8 -*-
# @Time    : 2019/5/7 14:58
# @Author  : zhu733756
# @FileName: tools.py

import codecs
try:
    from server.config import *
except:
    from NovelEditorServer.server.config import *
import os
import subprocess

def get_tinymce_store_path():
    '''获取作者文档保存路径'''
    if not os.path.exists(CUSTOM_FILE_BASE_DIR):
        try:
            #linux
            cmd='touch {}'.format(CUSTOM_FILE_BASE_DIR)
            r=subprocess.Popen(cmd, shell=True, errors=subprocess.PIPE)
            #windows
            if r.stderr is None:
                os.chdir(os.path.dirname(CUSTOM_FILE_BASE_DIR))
                subprocess.Popen('copy nul {}'.format("customPath.txt"), shell=True, errors=subprocess.PIPE)
        except:
            pass
        return DEFAULT_CUSTOM_FILE_BASE_DIR
    base_path = codecs.open(CUSTOM_FILE_BASE_DIR, mode="r", encoding='utf8').read().strip()
    return base_path if base_path else DEFAULT_CUSTOM_FILE_BASE_DIR


def find_folder_and_file(path,res=[],s=set(),filter_type="html"):
    '''递归寻找文件夹和文件txt，用来确认是书籍还是文章'''
    if not os.path.exists(path):
        return {"status":404,"res":"path not exist!"}
    for son_file in os.listdir(path):
        if son_file == "customPath.txt":
            continue
        sonfile_path=os.path.join(path,son_file)
        #head:斗破苍穹
        head=path[len(get_tinymce_store_path()):].lstrip("\\")

        if os.path.isfile(sonfile_path):
            if not son_file.endswith(filter_type):
                #ignore files not end with filter_type
                continue
            # filename:第一章
            filename=son_file.split(".")[0]
            if head in s:
                for r in res:
                    if head == r["mode"]:
                        r["files"].append(filename)
            else:
                res.append({
                    "mode": head,
                    "files": [filename]
                })
                s.add(head)
        elif os.path.isdir(sonfile_path):
            if os.listdir(sonfile_path):
                find_folder_and_file(sonfile_path,res=res,s=s)
            else:
                res.append({
                    "mode": son_file,
                    "files": []
                })

def find_folder_and_file_tools(path=None):
    path=path if path else get_tinymce_store_path()
    res=[]
    s=set()
    find_folder_and_file(path,res,s)
    return res


if __name__ == '__main__':
    #test find_folder_and_file
    res = []
    find_folder_and_file(get_tinymce_store_path(), res)
    print(res)


