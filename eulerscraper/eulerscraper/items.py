import re

import scrapy
from scrapy.loader.processors import MapCompose, Compose
from w3lib.html import remove_tags


def extract_first_number(text):
    i = re.search('\d+', text)
    return int(text[i.start():i.end()])


def array_to_value(element):
    return element[0]


class Problem(scrapy.Item):
    id = scrapy.Field(
        input_processor=MapCompose(remove_tags, extract_first_number),
        output_processor=Compose(array_to_value)
    )
    title = scrapy.Field(input_processor=MapCompose(remove_tags))
    content = scrapy.Field()