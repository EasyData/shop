# -*- coding: utf-8 -*-

import scrapy
import time
import urlparse

from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Join, MapCompose, TakeFirst
from scrapy.http import Request
from scrapy.spiders import CrawlSpider, Rule
from w3lib.html import remove_tags

from shop.items import ShopItem


class ForzieriEnSpider(CrawlSpider):

    name = 'forzieri_en'
    lang = 'en'

    allowed_domains = ['forzieri.com']
    start_urls = ['http://www.forzieri.com/?noipredirect=1']

    rules = (
        Rule(LinkExtractor(restrict_css=r'ul.global-nav>li.navitem')),
        Rule(LinkExtractor(restrict_css=r'ul.navigation_tree>li')),
        Rule(LinkExtractor(restrict_css=r'.pagination .next-page')),
        Rule(LinkExtractor(restrict_css=r'.product_list .product_list_item_info>a'), callback='parse_item'),
    )

    def parse_item(self, response):

        loader = ItemLoader(item=ShopItem(), response=response)
        loader.add_css('id', '#breadcrumbs .last-child::text')
        loader.add_value('url', response.url)
        loader.add_css('brand', '.productTitle>.brand_name>a::text')
        loader.add_css('name', '.productTitle>h1::text')
        loader.add_css('desc', 'p[itemprop="description"]')
        loader.add_css('cate', '#breadcrumbs span[itemprop="title"]::text', Join())
        loader.add_value('site', 'forzieri')
        loader.add_value('lang', self.lang)
        loader.add_value('time', time.time())

        url = urlparse.urljoin(
            self.start_urls[0],
            response.css('#scheda_tecnica_tab_trigger::attr(href)').extract_first(),
        )
        return Request(url, meta={'loader': loader}, callback=self.parse_item_ajax)

    def parse_item_ajax(self, response):

        loader = response.meta.get('loader')
        desc = loader.get_output_value('desc')
        desc += response.css('table').extract()
        loader.replace_value('desc', desc, MapCompose(remove_tags, unicode.strip), Join())
        return loader.load_item()


class ForzieriZhSpider(ForzieriEnSpider):

    name = 'forzieri_zh'
    lang = 'zh'

    start_urls = ['http://www.cn.forzieri.com/']
