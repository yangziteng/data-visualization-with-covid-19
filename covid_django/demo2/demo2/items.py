# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ChinaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # name = scrapy.Field()
    # price = scrapy.Field()
    # area = scrapy.Field()
    cn_jwsrNum = scrapy.Field()
    cn_heconNum = scrapy.Field()
    cn_conNum = scrapy.Field()
    cn_cureNum = scrapy.Field()
    cn_deathNum = scrapy.Field()
    cn_addjwsrNum = scrapy.Field()
    cn_province_econNum = scrapy.Field()
    cn_contactNum = scrapy.Field()
    ymd = scrapy.Field()
class WorldItem(scrapy.Item): 
    die =scrapy.Field()
    certain = scrapy.Field()
    recure = scrapy.Field()
    die_inc = scrapy.Field()
    recure_inc = scrapy.Field()
    certain_inc = scrapy.Field()
    date = scrapy.Field()
class CountryItem(scrapy.Item): 
    conNum =scrapy.Field() #确诊
    conadd = scrapy.Field() #新增
    cureNum = scrapy.Field() #治愈
    deathNum = scrapy.Field() #死亡
    name = scrapy.Field() #国家名字
class ProvinceItem(scrapy.Item): 
    cureNum =scrapy.Field() #累计治愈
    deathNum = scrapy.Field() #累计死亡
    econNum = scrapy.Field() #现存确诊
    jwsrNum = scrapy.Field() #境外输入
    value = scrapy.Field() #累计确诊
    name = scrapy.Field() #城市名字