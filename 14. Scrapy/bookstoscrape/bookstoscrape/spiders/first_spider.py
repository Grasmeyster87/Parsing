import scrapy


class FirstSpiderSpider(scrapy.Spider):
    name = "first_spider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        books = response.xpath("//ol[@class='row']/li")
        for book in books:
            yield {
                'title': book.xpath(".//h3/a/@title").get(),
                'price': book.xpath(".//p[@class='price_color']/text()").get(),
            }
