# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    page = scrapy.Field()
    rank = scrapy.Field()
    asin = scrapy.Field()
    pass
