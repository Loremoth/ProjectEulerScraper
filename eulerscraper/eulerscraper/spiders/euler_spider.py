# -*- coding: utf-8 -*-

import requests
import scrapy

from scrapy.loader import ItemLoader

from eulerscraper.items import Problem


def start_urls_detection():
    su = ['https://projecteuler.net/archives', 'https://projecteuler.net/archives;page=2']
    i = 1

    while True:
        request = requests.get(su[i])

        if request.status_code != 200:
            break

        i += 1
        su.append('https://projecteuler.net/archives;page=' + str(i + 1))

    return su


class EulerSpider(scrapy.Spider):
    name = 'euler'
    allowed_domains = ['projecteuler.net']
    start_urls = ["https://projecteuler.net/archives"]

    def parse(self, response):
        numpag = response.css("div.pagination a[href]::text").extract()
        maxpag = int(numpag[len(numpag) - 1])

        for href in response.css("table#problems_table a::attr(href)").extract():
            next_page = "https://projecteuler.net/" + href
            yield response.follow(next_page, self.parse_problems)

        for i in range(2, maxpag + 1):
            next_page = "https://projecteuler.net/archives;page=" + str(i)
            yield response.follow(next_page, self.parse_next)

        return [scrapy.Request("https://projecteuler.net/archives", self.parse)]

    def parse_next(self, response):
        for href in response.css("table#problems_table a::attr(href)").extract():
            next_page = "https://projecteuler.net/" + href
            yield response.follow(next_page, self.parse_problems)

    def parse_problems(self, response):
        l = ItemLoader(item=Problem(), response=response)
        l.add_css("title", "h2")
        l.add_css("id", "#problem_info")
        l.add_css("content", ".problem_content")

        yield l.load_item()