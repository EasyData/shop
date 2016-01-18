# -*- coding: utf-8 -*-

import scrapy
import time

from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Join, MapCompose, TakeFirst
from scrapy.http import FormRequest
from scrapy.spiders import CrawlSpider, Rule
from w3lib.html import remove_tags

from shop.items import ShopItem


class ShopbopEnSpider(CrawlSpider):

    name = 'shopbop_en'
    lang = 'en'

    allowed_domains = ['shopbop.com']
    start_urls = ['https://www.shopbop.com/']

    rules = (
        Rule(LinkExtractor(restrict_css=r'#topNavTile .link[data-at="shopall"]')),
        Rule(LinkExtractor(restrict_css=r'.pagination .next')),
        Rule(LinkExtractor(restrict_css=r'#product-container .url'), callback='parse_item'),
    )

    def start_requests(self):

        yield FormRequest(
            'https://www.shopbop.com/actions/i18n/updateShoppingPreferences',
            formdata={
                'savedPreferencesExist': 'true',
                'returnToUrl': '%2F',
                'page.locationCode': 'US',
                'page.languageCode': self.lang.upper(),
                'page.currencyCode': 'USD',
            })

    def parse_item(self, response):

        loader = ItemLoader(item=ShopItem(), response=response)
        loader.add_value('id', response.url, re=r'/([0-9]+).htm\?')
        loader.add_value('url', response.url)
        loader.add_css('brand', '#product-information h1 .row[itemprop="brand"]::text', TakeFirst(), unicode.strip)
        loader.add_css('name', '#product-information h1 .row[itemprop="name"]::text', TakeFirst(), unicode.strip)
        loader.add_css('desc', 'div[itemprop="description"]', TakeFirst(), remove_tags, unicode.strip)
        loader.add_css('cate', '.breadcrumb-list .breadcrumb span::text', Join())
        loader.add_value('site', 'shopbop')
        loader.add_value('lang', self.lang)
        loader.add_value('time', time.time())
        return loader.load_item()


class ShopbopZhSpider(ShopbopEnSpider):

    name = 'shopbop_zh'
    lang = 'zh'

