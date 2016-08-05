#coding = utf-8
'''
Created on 2015-8-28

@author: songhw
'''
import scrapy.cmdline

if __name__ == '__main__':
    scrapy.cmdline.execute(argv=['scrapy','crawl','reclusive'])
#     scrapy.cmdline.execute(argv=['scrapy','crawl','toDB'])
#     scrapy.cmdline.execute(argv=['scrapy','crawl','rTest'])