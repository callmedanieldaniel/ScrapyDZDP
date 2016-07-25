# -*- coding: utf-8 -*-
import json
from asyncore import dispatcher
from twisted.test.test_adbapi import SQLite3Connector



import pymongo
from scrapy_dev import settings
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class saveToJsonFile(object):
    
    def __init__(self):
        self.file = open('items.jl','wb')
    
    def process_item(self, item, spider):
        
        line = json.dump(dict(item)) + "\n"
        print "____________________________________________________________________________-"
        print line
        self.file.write(line)
        return item


# def saveToMysql(object):
#     def __init__(self):
#         self.conn = None
#         dispatcher.connect(self.ini, address)
#         
#     def initialize(self):
#         if path.exists(self.filename):
#             self.conn = SQLite3Connector.con

import pymongo
from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log
class MongoDBPipeline( object ):
   def __init__( self ):
       connection = pymongo.Connection(
                                     settings[ 'MONGODB_SERVER' ],
                                     settings[ 'MONGODB_PORT' ]
                                     )
       db = connection[settings[ 'MONGODB_DB' ]]
       self .collection = db[settings[ 'MONGODB_COLLECTION' ]]
    def process_item( self , item, spider):
        valid = True
         for data in item:
           if not data:
             valid = False
             raise DropItem( "Missing {0}!" . format (data))
         if valid:
           self .collection.insert( dict (item))
           log.msg( "Question added to MongoDB database!" ,
               level = log.DEBUG, spider = spider)
         return item

     