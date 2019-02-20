# -*- coding: utf-8 -*-
import scrapy


class WatchSpider(scrapy.Spider):
    name = 'watch'
    allowed_domains = ['www.marktplaats.nl']
    start_urls = ['http://www.marktplaats.nl/']

    def parse(self, response):
        pass
