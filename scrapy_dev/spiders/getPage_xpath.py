#coding:utf-8

from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy_dev.items import RegionItem


class DpToFileSpider(Spider):
    name = "toFile"
                   
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
            region['name'] = site.xpath('a/text()').extract()   
            region['href'] = site.xpath('a/@href').extract()
            #region['abUrl'] = site.xpath('text()').re('-\s[^\n]*\\r')
            items.append(region)    
            print region
            with open('region.txt','a+') as f:
                f.write(region['name'][0].encode('utf-8'))
                f.write(":")
                f.write(region['href'][0].encode('utf-8'))
                f.write(",")
        with open('region.txt','r') as f:
            print f.read()

        return items

    
