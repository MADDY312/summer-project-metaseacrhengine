import scrapy
from scrapy_splash import SplashRequest

class DataExtSpider(scrapy.Spider):
    name = 'data_ext'
    allowed_domains = ['myntra.com']
    script='''
    function main(splash,args) 
        splash.private_mode_enabled = false
    '''
    #deep link which will come from the frontend
    def start_requests(self):
        yield SplashRequest(url='https://www.fabindia.com/cotton-nagari-elasticated-pyjama-10683619',callback=self.parse,endpoint='render.html',
           args={
            'lua_source':self.script,
            'engine':'chromium',
            'wait': 0.5})
        

    def parse(self, response):
        yield{
            'title': response.xpath("(//h1[@itemprop='name']/text())[2]").get()
        }
        
