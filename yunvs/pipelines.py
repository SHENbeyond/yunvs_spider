# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class YunvsPipeline(object):
	def __init__(self):
		self.file = open('stock_list_result_20151109.txt','w')
		
	def process_item(self, item, spider):
		self.file.write(item['name'].strip()+'\t'+item['number'].strip()+'\t'+item['label'].encode('utf-8')+'\n')
		return item
