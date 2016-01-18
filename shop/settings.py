# -*- coding: utf-8 -*-

BOT_NAME = 'shop'
LOG_LEVEL = 'INFO'
SPIDER_MODULES = ['shop.spiders']
NEWSPIDER_MODULE = 'shop.spiders'
USER_AGENT = 'Mozilla/5.0'
ITEM_PIPELINES = {
    'shop.pipelines.ShopPipeline': 300,
}
