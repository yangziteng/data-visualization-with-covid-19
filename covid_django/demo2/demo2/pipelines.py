# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sys
import os
import django
sys.path.insert(0,os.path.dirname(os.getcwd()))
# useful for handling different item types with a single interface
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "covid_django.settings")# project_name 项目名称
django.setup()
# import models
from covid.models import ChinaCov,WorldCov,CountryCov,ProvinceCov
import pymysql

       
class mysqlPileLine:
    conn = None
    cursor = None
    def open_spider(self,spider):
        #初始化数据库的数据
        self.conn = pymysql.connect(host="localhost",user='root',passwd='root',port=3306,charset='utf8mb4',database='cov2')
        self.cursor  = self.conn.cursor()
    def process_item(self, item, spider):
        if (spider.name=="ChinaCov") :
   
            ChinaCov.objects.update_or_create(
                cn_jwsrNum = item["cn_jwsrNum"][0],
                cn_heconNum = item["cn_heconNum"][0],
                cn_conNum = item["cn_conNum"][0],
                cn_deathNum = item["cn_deathNum"][0],
                cn_addjwsrNum = item["cn_addjwsrNum"][0],
                cn_contactNum = item["cn_contactNum"][0],
                cn_cureNum = item["cn_cureNum"][0],
                cn_province_econNum = item["cn_province_econNum"][0],
                ymd = item["ymd"]
            )

            return item
        if spider.name=="CovWorld":
            WorldCov.objects.update_or_create(
               die = item["die"][0],
                certain = item["certain"][0],
                die_inc = item["die_inc"][0],
                recure = item["recure"][0],
                recure_inc = item["recure_inc"][0],
                certain_inc = item["certain_inc"][0],
                date = item["date"]
            )
            return item 
        if spider.name=="CountryCov":

            CountryCov.objects.update_or_create(
               conNum = item["conNum"][0],
                conadd = item["conadd"][0],
                cureNum = item["cureNum"][0],
                deathNum = item["deathNum"][0],
                name = item["name"][0],
            )  
            return item
        if spider.name == "ProvinceCov":
            ProvinceCov.objects.update_or_create(
                        cureNum = item["cureNum"][0],
                            deathNum = item["deathNum"][0],
                            econNum = item["econNum"][0],
                            jwsrNum = item["jwsrNum"][0],
                            value = item["value"][0],
                            name = item["name"],
                        )  
            return item
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()
        print("爬虫结束~")
