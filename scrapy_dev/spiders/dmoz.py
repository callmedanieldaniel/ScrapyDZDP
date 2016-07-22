from scrapy.spiders import Spider
from scrapy.selector import Selector

class DmozSpider(Spider):
    name = "dmoz"
                   
    allowed_domains = ["dianping.com"]
    start_urls = [
        "http://www.dianping.com/beijing"
    ]
    def parse(self, response):
#        filename = response.url.split("/")[-2]
#        with open(filename, 'wb') as f:
#            f.write(response.body)
            
        sel = Selector(response)
        sites = sel.xpath('//ul/li[2]/ul[@id=\"hotregion\"]/li')


        for site in sites:
            title = site.xpath('a/text()').extract()  
            link = site.xpath('a/@href').extract()  
            desc = site.xpath('text()').extract()              
            
            print "----------------------------"
            print title,link,desc
            
            
#        items = []
#            item = Website()
#            item['name'] = site.xpath('a/text()').extract()
#            
#            item['url'] = site.xpath('a/@href').extract()
#            item['description'] = site.xpath('text()').re('-\s[^\n]*\\r')
#            items.append(item)

#        return items

    
