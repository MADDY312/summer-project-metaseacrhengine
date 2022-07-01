import scrapy
import time
from selenium.webdriver.common.by import By
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from shutil import which

class test_2(scrapy.Spider):
    name='test_2'
    #allowed_domains=[]
    start_urls=[
        'https://www.jackjones.in/st-search?q=shoes'
        ]
    
    def hello(self):
        print("test-1")
        chrome_options=Options()
        chrome_options.add_argument("--headless")
        
        driver=webdriver.Chrome("C:/chromedriver")
       # print("test-2")
        #driver.set_window(1920,1080)
        driver.get("https://www.jackjones.in/st-search?q=shoes")
        print("test-2")
        time.sleep[3]
        tab=driver.findElement(By.xpath("//a[@class='st-single-product']"))
        tab[4].click()
        time.sleep[3]
        print("test-4")
        #driver.close()
        return driver.page_source
    
    def parse(self,response):
        print("test-3")
        resp=Selector(text=self.hello())
        yield{
            'title':resp.xpath("//h1/text()").get()
        }

