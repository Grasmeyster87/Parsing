import scrapy
import json
import time
import re

class GITSpider(scrapy.Spider):
    name = "GitHub"
    allowed_domains = ["github.com"]
    start_urls = ["https://github.com/trending"]

    # save link
    # def parse(self, response):
    #     for res in response.xpath("//h2[@class='h3 lh-condensed']"):
    #         repo_name = ''.join(res.xpath(".//a//text()").getall()).strip()
    #         repo_name = re.sub(r'\s+', ' ', repo_name).strip()


    #         repo_url = response.urljoin(res.xpath("./a/@href").get())
    #         yield {
    #             "name": repo_name.strip() if repo_name else None,
    #             "url": repo_url,
    #         }

    # def print_res():
    #     #выводим значение из каждого объекта в файле
    #     with open('github_link.json') as f:
    #         data = json.load(f)

    #     for item in data:
    #         res = f"This is res {item.key.strip()} : {item.values}"
    #         # res= str(item)
    #     time.sleep(5)
    #     print (res) 

    #save image
    # def parse(self, response):
    #     for image_url in response.css("img::attr(src)").getall():
    #         if not image_url.startswith('https'):
    #             image_url = response.urljoin(image_url)
    #         yield scrapy.Request(image_url, self.save_image)
    
    # def  save_image(self, response):
    #     filename = response.url.split("/")[-1]
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
    #     self.log('Saved file %s' % filename)

    #save image for all page
    def parse(self, response):
        links = response.css("a::attr(href)").getall()
        for link in links:
            yield scrapy.Request(response.urljoin(link), self.parse)

        for image_url in response.css("img::attr(src)").getall():
            if not image_url.startswith('https'):
                image_url = response.urljoin(image_url)
            yield scrapy.Request(image_url, self.save_image)
    
    def  save_image(self, response):
        filename = response.url.split("/")[-1]
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)