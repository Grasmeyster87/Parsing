import scrapy


class QuoteSpider(scrapy.Spider):
    name = "quote"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                'author': quote.css("small.author::text").get(),
                'text' : quote.css("span.text::text").get(),
                'tags' : quote.css("div.tags a::text").getall(),
            }
            yield from response.follow_all(css='ul.pager a', callback=self.parse)
