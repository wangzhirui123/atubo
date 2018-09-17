# # -*- coding: utf-8 -*-
# __author__ = 'Px'
#
# import sys
# import nltk
# import urllib2
# import csv
# import re
# import time
# import requests
# import MySQLdb
# from lxml import etree
# from bs4 import BeautifulSoup
# from nltk.tokenize import sent_tokenize
# reload(sys)
# sys.setdefaultencoding('utf8')
#
# def fenci():
#     response = urllib2.urlopen('http://author.baidu.com/home/1549973366214576')
#     html = response.read()
#     soup = BeautifulSoup(html)
#     clean = soup.get_text()
#     tokens = [tok for tok in clean.split()]
#     return tokens
#
# def tj_python():
#     '''
#     统计单词次数
#     '''
#     num_dic = {}
#     for tok in fenci():
#         if tok in num_dic:
#             num_dic[tok] +=1
#         else:
#             num_dic[tok] = 1
#     print num_dic
#
# def tj_nltk():
#     '''
#     NLTK统计词频
#     '''
#     Freq_dict_nltk = nltk.FreqDist(fenci())
#     for k,y in Freq_dict_nltk.items():
#         print str(k),str(y)
#
# def nltk_img():
#     Freq_dict_nltk = nltk.FreqDist(fenci())
#     Freq_dict_nltk.plot(50)
#
# def CsvPase():
#     '''
#     解析csv文件
#     '''
#     with open(u'C:/Users/13717/Desktop/OSSKey.csv','rb')as f:
#         reader = csv.reader(f)
#         for line in reader:
#             print line
#
# def yujucheck():
#     text = 'This is an example sent. The sentence splitter will split on sent markers. Ohh really !!'
#
#     all_sent = sent_tokenize(text)
#     print len(all_sent)
#     print all_sent
#
# def cut_txt(old_file):
#     import jieba
#     global cut_file     # 分词之后保存的文件名
#     cut_file = old_file + '_cut.txt'
#     try:
#         fi = open(old_file, 'r', encoding='utf-8')
#     except BaseException as e:  # 因BaseException是所有错误的基类，用它可以获得所有错误类型
#         print(Exception, ":", e)    # 追踪错误详细信息
#
#     text = fi.read()  # 获取文本内容
#     new_text = jieba.cut(text, cut_all=False)  # 精确模式
#     str_out = ' '.join(new_text).replace('，', '').replace('。', '').replace('？', '').replace('！', '') \
#         .replace('“', '').replace('”', '').replace('：', '').replace('…', '').replace('（', '').replace('）', '') \
#         .replace('—', '').replace('《', '').replace('》', '').replace('、', '').replace('‘', '') \
#         .replace('’', '')     # 去掉标点符号
#     fo = open(cut_file, 'w', encoding='utf-8')
#     fo.write(str_out)
#
# def model_train(train_file_name, save_model_file):  # model_file_name为训练语料的路径,save_model为保存模型名
#     from gensim.models import word2vec
#     import gensim
#     import logging
#     # 模型训练，生成词向量
#     logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
#     sentences = word2vec.Text8Corpus(train_file_name)  # 加载语料
#     model = gensim.models.Word2Vec(sentences, size=200)  # 训练skip-gram模型; 默认window=5
#     model.save(save_model_file)
#     model.wv.save_word2vec_format(save_model_file + ".bin", binary=True)   # 以二进制类型保存模型以便重用
#
# if __name__ == '__main__':
#
#     # from gensim.models import word2vec
#     # import os
#     # import gensim
#     #
#     # # if not os.path.exists(cut_file):    # 判断文件是否存在，参考：https://www.cnblogs.com/jhao/p/7243043.html
#     # cut_txt('result.txt')  # 须注意文件必须先另存为utf-8编码格式
#     #
#     # save_model_name = '倚天屠龙记.model'
#     # if not os.path.exists(save_model_name):     # 判断文件是否存在
#     #     model_train(cut_file, save_model_name)
#     # else:
#     #     print('此训练模型已经存在，不用再次训练')
#     #
#     # # 加载已训练好的模型
#     # model_1 = word2vec.Word2Vec.load(save_model_name)
#     # # 计算两个词的相似度/相关程度
#     # y1 = model_1.similarity("赵敏", "韦一笑")
#     # print(u"赵敏和韦一笑的相似度为：", y1)
#     # print("-------------------------------\n")
#     #
#     # # 计算某个词的相关词列表
#     # y2 = model_1.most_similar("张三丰", topn=10)  # 10个最相关的
#     # print(u"和张三丰最相关的词有：\n")
#     # for item in y2:
#     #     print(item[0], item[1])
#     # print("-------------------------------\n")
#     #
#
#
#     import synonyms
#     import jieba
#     words = jieba.cut('蚂蚁匠人网于2016年11月在北京创建，是目前国内著名建筑全流程分类信息B2B网站。作为信息平台，蚂蚁匠人网为用户提供建筑信息资源，如建筑材料及机械、设计服务等业务。蚂蚁匠人网在国内城市有10余个分部，为推动传统建筑行业转型，贡献自己的一份力。')
#     # print synonyms.display('当前')
#
#     for i in words:
#
#         try:
#             if len(i) < 2:
#                 continue
#             print synonyms.nearby(i)[0][1],(i),
#         except:
#             continue
#     # print synonyms.nearby('我国')[0][1]
#
#
