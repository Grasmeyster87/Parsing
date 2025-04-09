# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# переименовали в клас Product
class Product(scrapy.Item):
    # product_url = scrapy.Field()
    title = scrapy.Field()
    # product_price = scrapy.Field()
    # images = scrapy.Field()
    # priduct_text_header = scrapy.Field()
    # priduct_text= scrapy.Field()
