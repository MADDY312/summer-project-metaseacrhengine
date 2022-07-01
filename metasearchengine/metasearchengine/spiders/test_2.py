import time
import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from shutil import which

class test_2(scrapy.Spider):
    name='test_2'
    #allowed_domains=[]
    start_urls=['https://www.jackjones.in/st-search?q=shoes']

    def _init_(self):
        chrome_options=Options()
        chrome_options.add_argument("--headless")
        
        driver=webdriver.Chrome("C:/chromedriver")
        driver.set_window(1920,1080)
        driver.get("https://www.jackjones.in/st-search?q=shoes")
        tab=driver.find_elements_by_class_name("st-single-product")
        tab[4].click()

        self.html=driver.page_source
        driver.close()
    
    def parse(self, response):
        resp=Selector(text=self.html)
        yield{
            'title':resp.xpath("//h1/text()").get()
        }

