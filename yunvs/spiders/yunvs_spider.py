# -*- coding: utf-8 -*-
import scrapy
from yunvs.items import YunvsItem
from scrapy.selector import Selector
import traceback
import time
import re
import os,sys

class YunvsSpider(scrapy.Spider):
    name = "yunvs"
    allowed_domains = ["www.yuncaijing.com"]
    start_urls = (
        "http://www.yuncaijing.com/stock/index/600558",
    )
    def parse(self,response):
        path = os.path.abspath(os.path.dirname(sys.argv[0]))
        path_in = path +"/stock_list_20150914.txt"
        #path_in = "/data0/shenyanjun/spider/yunvs/stock_list_20150914.txt"
        items = [line.split('\t') for line in open(path_in,'r').readlines()]
        url_domain = "http://www.yuncaijing.com/stock/index/"
        for item in items:
            url_item = url_domain+item[0][2:]
            yield scrapy.Request(url_item,callback=self.parse_page,meta={'name':item[1],'number':item[0]})

    def parse_page(self,response):
        item = YunvsItem()
        res = Selector(response)
        item["name"] = response.meta['name']
        item["number"] = response.meta['number']
        #nodes = response.xpath('//div[@class="box1"]/div/div//a[@target="_blank"]/text()').extract()
        #result = [node.strip() for node in nodes][2:]
        result = response.xpath('//div[@class="concept tiny-text"]/a[@class="btn btn-primary"]/text()').extract()
        print "result:",result
        item["label"] = ';'.join(result)
        return item
