
from scrapy.spiders import Spider
from scrapy.selector import Selector



class DmozSpider(Spider):
    name = "example"
    allowed_domains = ["qfnu.edu.cn"]
    start_urls = [
#        "http://www.dianping.com/beijing",
        "http://www.qfnu.edu.cn/"        
       ]

    def parse(self , response):    

        sel = Selector(response)
        sites = sel.xpath("//ul/li")
        for site in sites:
            print "++++++++++++++++++++++++++++"
#            title = site.xpath("//a[contains(@href,'search')]/href()").extract() 
#            link = site.xpath("//a[contains(@href,'search')]/text()").extract() 
#            print "----------------------------"
#            print title,link          
            title = site.xpath("*//a/href()").extract() 
            link = site.xpath("*//a/text()").extract() 
            print "????????????????----------------"
            print title,link