# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from scrapy.item import Item,Field


class DmozItem(Item):
    name = Field()
    description = Field()
    url = Field()
    
class RegionItem(Item):
    name = Field()
    href = Field()
    abUrl = Field()
    
class ShopItem(Item):
    name = Field()
    href = Field()
    region_tag = Field()
    comment_title = Field()
    comment_num = Field()
    comment_meanPrice = Field()
    address = Field()
     
    