import scrapy
from scrapy import Request

class fliterextractor(scrapy.Spider):
    name = 'flit'
    
    count=0
    def start_requests(self):
        
        file_1=open(r'D:\list.txt','r')
        #print(file_1)
        while True:
            line =file_1.readline()
            
            #checking if line is empty
            if not line:
                break  
        
            t='https://www.google.com/search?q='   
            f=t+line.split('(')[0].replace(" ","+")+"+clothing"
            
            #headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
            allowed_domains=['google.com']
            new =line.split('(')[0].replace(" ","")
            new=new.lower()
            
            request=yield Request(f,meta = {'dont_redirect': True,'handle_httpstatus_list': [302]},callback= self.parse, cb_kwargs= {'newr':new})
            yield request    

        
    def parse(self, response,newr):
        newr:newr 
        yield {     
            'link': response.xpath("//a[contains(@href,newr)]/div/cite/text()").get()
         }   
    
               
       
       

