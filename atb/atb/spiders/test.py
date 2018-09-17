# # -*- coding: utf-8 -*-
# __author__ = 'Px'
#
# import sys
# import urllib2
# import re
# import time
# import requests
# import MySQLdb
# import random
# from lxml import etree
# from bs4 import BeautifulSoup
#
# reload(sys)
# sys.setdefaultencoding('utf8')
#
# def GetProxyIp():
#   result = str(requests.get('http://webapi.http.zhimacangku.com/getip?num=70&type=3&pro=&city=0&yys=0&port=1&pack=26384&ts=0&ys=0&cs=0&lb=2&sb=\n&pb=4&mr=1&regions=').content).replace('</br>','\n').split('\n')
#   # print result.split('\n')
#   # ip = random.choice(result)
#   return result
#
#
# def Test(ip):
#   proxies = {
#     'http': 'http://{}'.format(str(ip).strip()),
#   }
#   html = requests.get('http://ip.chinaz.com/',proxies=proxies).content
#   print html
#
# def BaiDuData():
#     MY_USER_AGENT = [
#     "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
#     "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
#     "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
#     "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
#     "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
#     "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
#     "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
#     "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
#     "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
#     "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
#     "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
#     "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
#     "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
#     "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
#     "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
#     "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
#     "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
#     "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
#     "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
#     "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
#     "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
#     "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
#     ]
#     a = 0
#     ip_list = []
#     while True:
#
#         headers = {
#           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#           'Accept-Encoding': 'gzip, deflate, br',
#           'Accept-Language': 'zh-CN,zh;q=0.9',
#           'Cache-Control': 'no-cache',
#           'Connection': 'keep-alive',
#           'Host': 'www.baidu.com',
#           'Pragma': 'no-cache',
#           'Upgrade-Insecure-Requests': '1',
#           # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'
#           'User-Agent': random.choice(MY_USER_AGENT)
#
#
#
#
#         }
#
#         url = 'https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&rsv_idx=2&tn=baiduhome_pg&wd=%E7%8E%8B%E5%BF%97%E9%94%90&rsv_spt=1&oq=%25E7%258E%258B%25E5%25BF%2597%25E9%2594%2590%25E7%259A%2584blog&rsv_pq=a7ca06aa00017cf1&rsv_t=efb9j0fVu7t%2FfKT7sHinWCTlwT3RIehu95DoYppjG%2FxcLTYOS2RLhustdCZ5LQl8JlEy&rqlang=cn&rsv_enter=0&inputT=1224&rsv_sug3=30&rsv_sug1=30&rsv_sug7=000&prefixsug=%25E7%258E%258B%25E5%25BF%2597%25E9%2594%2590&rsp=0&rsv_sug4=4992&rsv_sug=2'
#
#
#         url1 = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=2&tn=baiduhome_pg&wd=%E7%8E%8B%E5%BF%97%E9%94%90%E7%9A%84%E5%BE%AE%E5%8D%9A&rsv_spt=1&oq=%25E7%258E%258B%25E5%25BF%2597%25E9%2594%2590&rsv_pq=d0a735e000016845&rsv_t=7ec1IdNONGscbRqvol9Xt%2Blwj5M05z%2BKjr3W%2Birv1qTBY5xt95ERAWVElEEjfX1HeIiN&rqlang=cn&rsv_enter=0&inputT=4233&rsv_sug3=35&rsv_sug1=32&rsv_sug7=000&rsv_sug4=4561&rsv_sug=1'
#         if len(ip_list) == 0:
#             print '正在获取ip...'
#             ip_list = GetProxyIp()
#         ip = random.choice(ip_list)
#
#         proxies = {
#         'http': 'http://{}'.format(ip).strip(),
#       }
#         result = requests.get(url,proxies=proxies,headers=headers).content
#         result1 = requests.get(url1,proxies=proxies,headers=headers).content
#         if '<title>王志锐_百度搜索</title>' in result and '<title>王志锐的微博_百度搜索</title>' in result1:
#             a+=1
#
#             print 'IP:{}\t当前第%d次访问'.format(ip)%a
#             ip_list.remove(ip)
#         else:
#             print '访问失败'
#             ip_list.remove(ip)
#             continue
#
#
#
#
# BaiDuData()
# # Test(GetProxyIp())