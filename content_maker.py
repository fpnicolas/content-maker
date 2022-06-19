"""
根据文件夹内的书籍情况，建立目录甚至连接，供查找，可以称之为书架系统,
1生成系统；直接全体生成目录，使用xml或json来记录。
2更新系统，当检测到某个文件夹下有新增书目，则进行局部更新，这里面或许涉及hash值计算来提高速度
3显示系统，用来显示已有书目
"""

import os
import json

# path = r"C:\Users\fpnic\Documents\books"
path = r"E:\\"
bookshelf = {"books": []}
content_path = path + r'\content'


def add_to_shelf(path, bookshelf, book_list):
    books = [f for f in os.listdir(path) if os.path.isfile(path+"\\"+f) and f != 'content']
    book_list.extend(books)
    book_dirs = [f for f in os.listdir(path) if os.path.isdir(path+"\\"+f)]
    for book_dir in book_dirs:
        bookshelf[book_dir] = {"books": []}
        add_to_shelf(path+'\\'+book_dir, bookshelf[book_dir], bookshelf[book_dir]["books"])

    # 添加hash


add_to_shelf(path, bookshelf, bookshelf['books'])


def add_to_json(bookself):
    with open(content_path, "w") as f:
        json.dump(bookself, f, ensure_ascii=False, indent=4)


add_to_json(bookshelf)


def update_bookself(bookself_json):
    data = json.loads(bookself_json)
    print(data)
    #
