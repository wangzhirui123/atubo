# -*- coding: utf-8 -*-
__author__ = 'Px'

import sys
import pymongo
import re
import time
import requests
import MySQLdb
from lxml import etree
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf8')

def GetData():

    pass


if __name__ == '__main__':
    Client = pymongo.MongoClient()
    conn = MySQLdb.connect('101.201.70.139','root','Myjr678!@#','ant',charset='utf8')
    cur = conn.cursor()
    DB = Client['zhizaoDB']
    TB = DB['zhizaoTB']
    data = TB.find({})
    for i in data:
        sql_in = 'insert into dingyao(company_name,phone,fix_phone,contact_man,class_name)VALUES ("%s","%s","%s","%s","%s")'%(i['company_name'],i['phone'],i['fix_phone'],i['contact_man'],i['class_name'])
        cur.execute(sql_in)
        conn.commit()










