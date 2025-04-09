import scrapy
import json

#CrawlSpider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

# подключили поля Item
from scrapy.item import Item, Field  # библиотека позволяет задавать произвольные поля на файлы items

# подключили файл Item.py и импортировали Product поля
from newparce_project.items import Product
"""
scrapy.Spyder - стандартный паук
XMLFeedSpider - паук по xml файлам
CSVFeedSpider - паук по CSV файлам
SitemapSpider - число по sitemap.xml - datatime
CrawSpider - сборщик ссылок!    
"""
class ProdparSpider(CrawlSpider):
    name = "prodpar"
    allowed_domains = ["prodpar.com"]
    start_urls = ["https://scrapy.org/"]
    # start_urls = ["https://xn-----mlcmbbnctfc9anx4ak5a1d.xn--p1ai/catalog/metallicheskaya_mebel/"]

    """
    https://столешницы-и-кухни.рф/catalog/
    allow = ('') что будем обходить
    deny = ('?serch') запретить какието параметры
    callback = ('') передать в парсер
    follow=True - следовать по ссылке
    """

    """
    // h1
    //span[@class="priceContainer"]//span/text()

    xpath('')
    // - везде
    / - внутри 1
    ./ -внутри текущего тега
    ../ - в теге перед эти тегом.
    @ - классы атрибуты параметры
    """
    # rules = (Rule(LinkExtractor(allow=('podstolya'), deny=('/filter', '/?arrFilter', '/?register', '/auth', '/?backurl=', '/?forgot_password', '/?VIEW=LINE', '/?VIEW=TABLE', '/?VIEW=',)), callback='parse', follow=True),)
    rules = (Rule(LinkExtractor(), callback='parse', follow=True),)
    def parse(self, response):
        item = Product()
        item['product_url']= response.url
        item['title'] = response.xpath('//title/text()').getall()
        print(f"Parsed title: {item['title']}")
        # item['product_price']= response.xpath('//span[@class="priceContainer"]//span/text()').get()
        # item['images'] = response.xpath('//div[@class="pictureSlider"]//a/img/@src').get()
        # item['priduct_text_header'] = response.xpath('//div[@class="changeShortDescription"]/text()').get()
        # item['priduct_text'] = response.xpath('//div[@id="detailText"]/div/text()').get()

        #место для получения полного адреса картинки
        main_img_url = response.urljoin(response.xpath('//dev[@class="pictureSlider"]//a/img/@src').get())
        item['image_urls'] = [main_img_url]
        yield item
