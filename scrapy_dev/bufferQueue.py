# -*- coding: utf-8 -*-
from Queue import Queue  
from scrapy import item

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

class ItemQueue():
    regonItemQue = Queue() 
    shopItemQue = Queue()

def enQueRegion(item):
    ItemQueue.regonItemQue.put(item)

def deQueRegion():
    return ItemQueue.regonItemQue.get()

def enQueShop(item):
    ItemQueue.shopItemQue.put(item)

def deQueShop():
    return ItemQueue.shopItemQue.get()


