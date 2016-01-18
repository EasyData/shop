# -*- coding: utf-8 -*-


class ShopPipeline(object):

    def process_item(self, item, spider):
        for k, v in item.iteritems():
            item[k] = v[0]
        return item
