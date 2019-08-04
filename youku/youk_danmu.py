#coding:utf-8
import os
import time
import json
import random

import jieba
import requests
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# 词云形状图片
WC_MASK_IMG = 'wawa.jpg'
# 评论数据保存文件
COMMENT_FILE_PATH = 'youku_danmu.txt'
# 词云字体
#WC_FONT_PATH = '/Library/Fonts/Songti.ttc'
WC_FONT_PATH ='C:\Windows\Fonts\simfang.ttf'


def spider_danmu(mat=0):
    url='https://service.danmu.youku.com/list?jsoncallback=jQuery111207778176652709636_1563676684228&mat=%s&mcount=1&ct=1001&iid=1055639208&aid=329784&cid=97&lid=0&ouid=0&_=1563676684250' %mat
    kv = {'user-agent': 'Mozilla/5.0', 'Referer': 'https://v.youku.com/v_show/id_XNDIyMjU1NjgzMg==.html?spm=a2ha1.12675304.m_2556_c_8261.d_2&s=a4de6bdc5675415ea280&scm=20140719.manual.2556.show_a4de6bdc5675415ea280'}

    try:
        r = requests.get(url, headers=kv)
        #返回状态
        r.raise_for_status()
    except:
        print('爬取失败')
    # 截取json数据字符串(前面多少位，后面多少位)
    json_start_index=r.text.index('(')+1
    r_json_str = r.text[json_start_index:-2]
    print('================'+r_json_str)
    # 字符串转json对象
    r_json_obj = json.loads(r_json_str)
    #如果请求的总数count=0说明弹幕已经获取完
    if not r_json_obj['result']:
        return 0
    # 获取评价列表数据
    r_json_danmus = r_json_obj['result']
    # 遍历评论对象列表
    for r_json_danmu in r_json_danmus:
        # 以追加模式换行写入每条评价
        with open(COMMENT_FILE_PATH, 'a+') as file:
            try:
                file.write(r_json_danmu['content'] + '\n')
            except:
                print(print('-------------'+r_json_danmu['content']))
        # 打印评论对象中的评论内容
        print(r_json_danmu['content'])
    return 1

def batch_spider_danmu():
    """
    批量爬取
    """
    # 写入数据前先清空之前的数据
    if os.path.exists(COMMENT_FILE_PATH):
        os.remove(COMMENT_FILE_PATH)
    i=0;
    while spider_danmu(i):
        time.sleep(random.random()*5)
        i+=1





def cut_word():
    """
    对数据分词
    :return: 分词后的数据
    """
    with open(COMMENT_FILE_PATH) as file:
        comment_txt = file.read()
        wordlist = jieba.cut(comment_txt, cut_all=True)
        wl = " ".join(wordlist)
        print(wl)
        return wl


def create_word_cloud():
    """
    生成词云
    :return:
    """
    '''数据清洗词列表'''
    stop_words=['哈哈','哈哈哈哈','哈哈哈','不是','为什么','什么','怎么','这个']

    # 设置词云形状图片
    #wc_mask = np.array(Image.open(WC_MASK_IMG))
    # 设置词云的一些配置，如：字体，背景色，词云形状，大小
    wc = WordCloud(background_color="white", max_words=2000, scale=4,
                   max_font_size=50, random_state=42, stopwords=stop_words,font_path=WC_FONT_PATH)
    # 生成词云
    wc.generate(cut_word())

    # 在只设置mask的情况下,你将会得到一个拥有图片形状的词云
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    #plt.figure()
    plt.show()


if __name__ == '__main__':
    # 爬取数据
    #batch_spider_danmu()

    # 生成词云
    create_word_cloud()
