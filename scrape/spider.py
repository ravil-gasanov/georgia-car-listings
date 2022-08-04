import scrapy
import json


class MyAutoSpider(scrapy.Spider):
    name = 'MyAutoSpider'
    page = 1
    start_urls = ['https://api2.myauto.ge/en/products?TypeID=0&ForRent=&Mans=&CurrencyID=3&MileageType=1&SortOrder=1&Page=1']

    def parse(self, response):
        data = json.loads(response.text)
        for car in data["data"]["items"]:
            yield car
        

        self.page += 1

        if self.page <= 9143:
            url = f"https://api2.myauto.ge/en/products?TypeID=0&ForRent=&Mans=&CurrencyID=3&MileageType=1&SortOrder=1&Page={self.page}"
            yield scrapy.Request(url=url, callback=self.parse)