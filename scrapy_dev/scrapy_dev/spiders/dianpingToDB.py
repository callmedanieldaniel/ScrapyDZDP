#coding:utf-8

from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy_dev.items import RegionItem

class DmozSpider(Spider):
    name = "tomysql"
                   
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
        return items

    
