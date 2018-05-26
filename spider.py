from firebase import firebase
import scrapy
import requests

db = firebase.FirebaseApplication('')
data = db.get('/posts', None)

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://ohmycode.com.br']

    def parse(self, response):
        for href in response.css("h1.title a::attr('href')"):
            url = response.urljoin(href.extract())
            
            if data is not None:
                created = 0
                for k in data:
                    if (type(data[k]) is dict):
                        if url == data[k].get('link'):
                            created = 1
                            break
                        else:
                            created = 0

                if created == 0:
                    result = db.post('/posts', {'link': url})

                    # Enviando mensagem via API do telegram
                    # requisicao = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text=Novo+post:{}".format(
                    #     "TOKEN", 
                    #     ID_CHANNEL,
                    #     url)

                    # requests.get(requisicao) 
                    
            else:
                result = db.post('/posts', {'link': url})
                