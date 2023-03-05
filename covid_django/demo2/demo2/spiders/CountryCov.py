import scrapy
import json
from .. import items
class CountrycovSpider(scrapy.Spider):
    name = 'CountryCov'

    start_urls = ['https://news.sina.com.cn/project/fymap/ncp2020_full_data.json?_=1674182940846&callback=jsoncallback']

    def parse(self, response):
        res = response.text
        res = res.replace("jsoncallback(","").replace(");","")
        res = json.loads(res)
        obj = res["data"]["otherlist"]
        item = items.CountryItem()
        for ik in obj:
            item["conNum"]=int(ik["conNum"]), 
            item["conadd"]=int(ik["conadd"]),
            item["cureNum"]=int(ik["cureNum"]),
            item["deathNum"]=int(ik["deathNum"]),
            item["name"]=ik["name"],
            yield item