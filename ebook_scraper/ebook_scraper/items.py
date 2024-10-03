# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field
from itemloaders.processors import MapCompose, TakeFirst

def get_price(text):
    return float(text.replace('£', ''))

class EbookScraperItem(Item):
    title = Field(output_processor=TakeFirst())
    price = Field(input_processor=MapCompose(get_price), output_processor=TakeFirst())
