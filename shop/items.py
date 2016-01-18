# -*- coding: utf-8 -*-

import scrapy


class ShopItem(scrapy.Item):

    id = scrapy.Field()
    url = scrapy.Field()
    brand = scrapy.Field()
    name = scrapy.Field()
    desc = scrapy.Field()
    cate = scrapy.Field()
    site = scrapy.Field()
    lang = scrapy.Field()
    time = scrapy.Field()
