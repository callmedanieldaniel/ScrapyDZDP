# -*- coding: utf-8 -*-

# Scrapy settings for stack project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'stack'

SPIDER_MODULES = ['stack.spiders']
NEWSPIDER_MODULE = 'stack.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'stack (+http://www.yourdomain.com)'


ITEM_PIPELINES = {'stack.pipelines.MongoDBPipeline':300, }

MONGODB_SERVER = "192.168.4.196"
MONGODB_PORT = 27017 
MONGODB_DB = "scrapy" 
MONGODB_COLLECTION = "dzdp_1"

# MONGODB_SERVER = "localhost"
# MONGODB_PORT = 27017
# MONGODB_DB = "stackoverflow"
# MONGODB_COLLECTION = "questions"



DOWNLOAD_DELAY = 5
