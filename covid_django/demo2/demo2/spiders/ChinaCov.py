import scrapy
from demo2.items import ChinaItem 
import json
class FirsSpider(scrapy.Spider):
    name = 'ChinaCov'
    start_urls = ['https://news.sina.com.cn/project/fymap/ncp2020_full_data.json?_=1671811786827&callback=jsoncallback']

    def parse(self, response):
        res = response.text
        res = res.replace("jsoncallback(","").replace(");","")
        obj = json.loads(res)
        his = obj['data']["historylist"]
        date = "2021.01.14"
        item = ChinaItem()

        for it in his:
            # if it["ymd"]<date:
            # try:
                item["cn_jwsrNum"]  = int(it["cn_jwsrNum"]),
                item["cn_heconNum"]  = int(it["cn_heconNum"]),
                item["cn_conNum"] = int(it["cn_conNum"]),
                item["cn_deathNum"]  = int(it["cn_deathNum"]),
                item["cn_cureNum"]  = int(it["cn_cureNum"]),
                item["cn_addjwsrNum"] = int(it["cn_addjwsrNum"]),
                item["cn_province_econNum"] = int(it["cn_province_econNum"]),
                if "cn_contactNum" in it:
                    item["cn_contactNum"] = int(float(it["cn_contactNum"])) ,
                else:
                    item["cn_contactNum"] = (0,) 
                item["ymd"] = it["ymd"]
                yield item
