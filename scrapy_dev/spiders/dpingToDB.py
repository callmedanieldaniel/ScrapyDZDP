#coding:utf-8

from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy_dev.items import RegionItem
from scrapy_dev.bufferQueue import enQueRegion, deQueRegion
from dmoz import DmozSpider
from getPage_xpath import DpToFileSpider

import json
from scrapy.crawler import CrawlerProcess

class DzdbSpider(Spider):
    name = "toDB"
                   
    allowed_domains = ["dianping.com"]
    start_urls = [
        "http://www.dianping.com/beijing"
    ]
    def parse(self, response):
            
        sel = Selector(response)
        sites = sel.xpath('//ul/li[2]/ul[@id=\"hotregion\"]/li')
        items =[] 
#        item = {'href': [u'/search/category/2/0/r1488'], 'name': [u'\u4e2d\u5173\u6751']}
           
        for site in sites:        
            region = RegionItem()
            region['name'] = site.xpath('.//a/text()').extract()   
            region['href'] = site.xpath('.//a/@href').extract()
            #region['abUrl'] = site.xpath('text()').re('-\s[^\n]*\\r')
            items.append(region)  
            enQueRegion(region)
            
#             jitem = json.dump(region,cls=RegionEncoder)                       
#             print "++++++",jitem

            print "-----",region,"|||",deQueRegion()
            
            with open('db.txt','a+') as f:
                f.write(region['name'][0].encode('utf-8'))
                f.write(":")
                f.write(region['href'][0].encode('utf-8'))
                f.write(",")
        with open('db.txt','r') as f:
            print f.read()

        return items


class RegionEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, RegionItem):
            return obj["name"][0].encode('utf-8')+","+obj["href"][0].encode('utf-8')
        return json.JSONEncoder.default(self, obj)


    

# process = CrawlerProcess()
# # process.crawl(DpToFileSpider)   
# process.crawl(DzdbSpider) 
# process.start()
    

    