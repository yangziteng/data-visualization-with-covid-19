import scrapy
import json

from .. import items
# from items import Demo3Item
class CovSpider(scrapy.Spider):
    name = 'CovWorld'
    start_urls = ['https://gwpre.sina.cn/ncp/foreign?_=1671780722926&callback=dataAPIData']

    def parse(self, response):
        res = response.text
        res=res.replace("try{dataAPIData(","")
        res=res.replace(");}catch(e){};","")
        obj = json.loads(res)
        his = obj["result"]["history"] 
        # date = "2021.01.14"
        for ik in his:
            # if ik["date"]<date:
                # print(ik)
                item = items.WorldItem()
                item["die"]=int(ik["die"]), 
                item["certain"]=int(ik["certain"]),
                item["recure"]=int(ik["recure"]),
                item["die_inc"]=int(ik["die_inc"]),
                item["recure_inc"]=int(ik["recure_inc"]),
                item["certain_inc"]=int(ik["certain_inc"]),
                item["date"]=ik["date"]
                yield item
                
        


