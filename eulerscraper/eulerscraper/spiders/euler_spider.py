# -*- coding: utf-8 -*-
import httplib2
import requests
from eulerscraper.items import Problem
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule


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


class EulerSpider(CrawlSpider):
    name = 'euler'
    allowed_domains = ['projecteuler.net']
    start_urls = start_urls_detection()

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        # Rule(LinkExtractor(allow=('category\.php',), deny=('subsection\.php',))),
        Rule(LinkExtractor(allow=('problem=\d*',)), callback="parse_problems"),
        Rule(LinkExtractor(allow=('archives;page=\d*',), unique=True), follow=True)
    )

    def parse_problems(self, response):
        l = ItemLoader(item=Problem(), response=response)
        l.add_css("title", "h2")
        l.add_css("id", "#problem_info")
        l.add_css("content", ".problem_content")

        yield l.load_item()

    # def parse_content(self, response):
    #     #return response.css("div.problem_content::text").extract()
    #     next_page = "https://projecteuler.net/archives;page=2"
    #     n = 3
    #
    #     while n < 14:
    #         next_page = response.urljoin(next_page)
    #         yield scrapy.Request(next_page, callback=self.parse)
    #         next_page = next_page[0:len(next_page) - 1] + str(n)
    #         n += 1
