import scrapy

class SiasdoSpider(scrapy.Spider):
    name = "siasdo"
    allowed_domains = ["siasdo.com.br"]
    start_urls = ["http://siasdo.com.br"]

    def parse(self, response):
        for sel in response.xpath('//section/div/ul/li'):
            desc = sel.xpath('text()').extract()
            print desc[0].encode('utf-8')
