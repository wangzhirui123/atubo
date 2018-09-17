# -*- coding: utf-8 -*-
import scrapy
import sys
from urlparse import urljoin
from atb.items import AtbItem

reload(sys)
sys.setdefaultencoding('utf8')

class AtbspiderSpider(scrapy.Spider):
    name = 'atbspider'
    allowed_domains = ['https://www.atobo.com.cn']
    start_urls = ['https://www.atobo.com.cn/Products/p11-c1049-y2/']

    def parse(self, response):
        for i in response.xpath('//div[@class="product_contextlist bphoto"]/ul/li/div/ul/li[2]/a/@href').extract():
            yield scrapy.Request(urljoin('https://www.atobo.com.cn/HotOffers/c324/',i),callback=self.parse_detail,dont_filter=True)
        next_page= urljoin('https://www.atobo.com.cn',response.xpath('//span[@class="page_next page-n"]/a/@href')[0].extract())

        yield scrapy.Request(next_page,callback=self.parse,dont_filter=True)


    def parse_detail(self,response):
        items = AtbItem()

        try:
            items['Class_name'] = response.xpath('//div[@class="cur_post"]/a[3]/text()')[0].extract()
            items['caption'] = response.xpath('//div[@class="product-name"]/ul/li[1]/text()')[0].extract()
            items['commpany'] = response.xpath('//div[@class="right-frame"]/ul[1]/li/a/text()')[0].extract()
        except:
            yield scrapy.Request(response.url,callback=self.parse_detail,dont_filter=True)


        items['keyword'] ='保温材料'
        items['address'] = response.xpath('//div[@class="right-contactinfo"]/ul[2]/li[2]/text()')[0].extract()
        items['phone'] = response.xpath('//li[@class="header-info"]/div/ul[2]/li/strong/text()')[0].extract()
        items['fixed_phone'] = response.xpath('//li[@class="header-info"]/div/ul[2]/li[2]/strong/text()')[0].extract()
        items['contact_man'] = response.xpath('//li[@class="header-info"]/div/ul/li[1]/text()')[0].extract()

        yield items
        # print items['Class_name'],items['caption'],items['keyword'],items['commpany'],items['address'],items['phone'],items['fixed_phone'],items['contact_man']



