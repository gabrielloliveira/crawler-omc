import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://ohmycode.com.br']

    def parse(self, response):
        for href in response.css("h1.title a::attr('href')"):
            url = response.urljoin(href.extract())
            yield {'link': url}

            