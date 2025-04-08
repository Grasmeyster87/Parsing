import scrapy
from scrapy_splash import SplashRequest
import base64
import json


class QtSplashSpider(scrapy.Spider):
    name = "qt_splash"
    allowed_domains = ["quotes.toscrape.com", "localhost"]
    # start_urls = ["https://quotes.toscrape.com/js/"]

    script = """
        function main(splash, args)
            url = args.url
            assert(splash:go(url))  
            assert(splash:wait(3))               
            return splash:html()
        end
    """

    def start_requests(self):
        yield SplashRequest(url='https://quotes.toscrape.com', callback=self.parse, endpoint='execute', args={'lua_source': self.script, 'wait': 4,})

    def parse(self, response):

        quotes = response.xpath("//div[@class='quote']")
        for quote in quotes:
            yield {
                'author': quote.xpath(".//small[@class='author']/text()").get(),
                'text': quote.xpath(".//span[@class='text']/text()").get(),
                'tags': quote.xpath(".//a[@class='tag']/text()").getall()
            }

        next_page = response.xpath("//li[@class='next']/a/@href").get()
        if next_page:
            url = response.urljoin(next_page)
            yield SplashRequest(url=url, callback=self.parse, endpoint='execute', args={'lua_source': self.script})

    