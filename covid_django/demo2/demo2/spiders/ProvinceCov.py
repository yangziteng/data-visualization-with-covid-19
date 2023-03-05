import scrapy
import json
from .. import items


class ProvincecovSpider(scrapy.Spider):
    name = 'ProvinceCov'
    start_urls = ['https://news.sina.com.cn/project/fymap/ncp2020_full_data.json?_=1674182940846&callback=jsoncallback']

    def parse(self, response):
        res = response.text
        res = res.replace("jsoncallback(","").replace(");","")
        res = json.loads(res)
        obj = res["data"]["list"]
        for ik in obj:
            # if ik["date"]<date:
                # print(ik)
                item = items.ProvinceItem()
                item["cureNum"]=int(ik["cureNum"]), 
                item["deathNum"]=int(ik["deathNum"]),
                item["econNum"]=int(ik["econNum"]),
                item["jwsrNum"]=int(ik["jwsrNum"]),
                item["value"]=int(ik["value"]),
                item["name"]=ik["name"]
                yield item