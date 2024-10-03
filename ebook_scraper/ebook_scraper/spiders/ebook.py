from scrapy import Spider
from ebook_scraper.items import EbookScraperItem
from scrapy.loader import ItemLoader


class EbookSpider(Spider):

    name = 'ebook'

    start_urls = ['https://books.toscrape.com', 'https://books.toscrape.com/catalogue/category/books/travel_2/index.html']

    def parse(self, response):
        print('[ OUR RESPONSE ]')
        
        books = response.css('article.product_pod')

        for book in books:
            loader = ItemLoader(item=EbookScraperItem(), selector=book)

            loader.add_css(field_name='title', css='h3 a::attr(title)')
            loader.add_css(field_name='price', css='p.price_color::text')

            yield loader.load_item()