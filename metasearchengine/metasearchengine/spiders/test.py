import scrapy
from scrapy_playwright.page import PageCoroutine

class ProductSpider(scrapy.Spider):
    name = 'test'

    def start_requests(self):
        yield scrapy.Request(
            'https://shoppable-campaign-demo.netlify.app/#/',
            meta={
                'playwright': True,
                'playwright_include_page': True,
                'playwright_page_coroutines': [
                    PageCoroutine("wait_for_selector", "div#productListing"),
                ]
            }
        )

    async def parse(self, response):
        yield{
            'title':response.text
        }