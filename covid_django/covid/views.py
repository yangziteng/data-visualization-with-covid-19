from django.http import Http404
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from . import models
# from . import serializers
from .settings import CACHE_PAGE_TIMEOUT
from django.http import HttpResponse

import json
def response_as_json(data):
    json_str = json.dumps(data)
    response = HttpResponse(
        json_str,
        content_type="application/json",
    )
    response["Access-Control-Allow-Origin"] = "*"
    return response


def json_response(data, code=200):
    data = {
        "code": code,
        "msg": "success",
        "data": data,
    }
    return response_as_json(data)


def json_error(error_string="error", code=500, **kwargs):
    data = {
        "code": code,
        "msg": error_string,
        "data": {}
    }
    data.update(kwargs)
    return response_as_json(data)

test_data = [
    {
        "globalStatistics": {
            "confirmedCount": 2913206,
            "curedCount": 826309,
            "deadCount": 206245,
            "seriousCount": 0,
            "currentConfirmedCount": 1880652,
            "suspectedCount": 0
        },
        "domesticStatistics": {
            "confirmedCount": 84341,
            "curedCount": 78558,
            "deadCount": 4643,
            "seriousCount": 974,
            "currentConfirmedCount": 1140,
            "suspectedCount": 1636
        },
        "internationalStatistics": {
            "confirmedCount": 2828865,
            "curedCount": 747751,
            "deadCount": 201602,
            "seriousCount": 0,
            "currentConfirmedCount": 1879512,
            "suspectedCount": 4
        },
        "modifyTime": "2020-04-30T01:12:33Z",
        "createTime": "2020-01-20T16:31:39Z"
    }
]
JsonResponse = json_response
JsonError = json_error
DEFAULT_COUNTRY_CODE = 'CHN'
EXCLUDE_COUNTRY_CODES = ('TWN', 'HKG', 'MAC')  # They belong to China.

class Test(APIView):
    def get(self, request, *args, **kwargs):
        return response_as_json(test_data)
class WorldTrendView(APIView):
    def get_World_obj(self):
        result = []
        values_fields = (
            'die', 'certain',
            'recure', 'die_inc', 'recure_inc',"certain_inc","date")
        res =  models.WorldCov.objects.all().order_by("date")
        for item in res.values_list(*values_fields):
            item = dict(zip(values_fields, item))
            statistics = {}
            for name, value in item.items():
                statistics[name] = value
            result.append(statistics)
        result = result[::-1]
        return result
    # def get(self,request):

    #     new_result = []
    #     result = self.get_World_obj()
    #     print(result)

    #     for item in result:
    #         obj = {}
    #         obj["confirmedCount"] = item["certain"]
    #         obj["curedCount"] = item["recure"]
    #         #当前确诊
    #         # obj["currentConfirmedCount"] 
    #         obj["deadCount"] = item["die"]
    #         d = item["date"].split(".")
    #         obj["dateId"] = int("".join(d))
    #         new_result.append(obj)
    #     new_result = new_result[::-1]
    #     return json_response(new_result)
    def get(self,request):
        obj = {
            "confirmedCountList":[],
            "curedCountList":[],
            "currentConfirmedCountList":[],
            "importedCountList":[],
            "importedIncrList":[],
            "currentConfirmedIncrList":[],
            "deadCount":[]
        }
        result = self.get_World_obj()
        for item in result:
            item["date"] = item["date"].split(".")
            item["date"] = item["date"][1]+"-"+item["date"][2]
            obj["confirmedCountList"].append([item["certain"],item["date"]])
            obj["curedCountList"].append([item["recure"],item["date"]]) 
            obj["deadCount"].append([item["die"],item["date"]])
        return json_response(obj)
class StatisticsChinaView(APIView):
    def get(self,request):
        result2 = {}
        #需求：获取12月18号的中国的数据和世界的数据
        res_china =  models.ChinaCov.objects.filter(ymd="2022.12.20").first()
        for field in models.ChinaCov._meta.fields:
            name = field.attname
            value = getattr(res_china, name)
            result2[name] = value
        all_data = {
            #  "domesticStatistics": {
            # "confirmedCount": result2["cn_conNum"],
            # "curedCount": result2["cn_cureNum"],
            # "deadCount": result2["cn_deathNum"],
            # "currentConfirmedCount": result2["cn_province_econNum"]
            "confirmedCount":result2["cn_conNum"],
            "confirmedIncr":result2["cn_contactNum"],
            "curedCount":result2["cn_cureNum"],
            "curedIncr":0,
            "deadCount":result2["cn_deathNum"],
            "importedCount":result2["cn_jwsrNum"]
        }
        # all_data = {
        #     #  "domesticStatistics": {
        #     # "confirmedCount": result2["cn_conNum"],
        #     # "curedCount": result2["cn_cureNum"],
        #     # "deadCount": result2["cn_deathNum"],
        #     # "currentConfirmedCount": result2["cn_province_econNum"]
        #     "confirmedCount":result2["cn_conNum"],
        #     "confirmedIncr":0,
        #     "curedCount":result2["cn_cureNum"],
        #     "curedIncr":0,
        #     "deadCount":result2["cn_deathNum"],
        #     "importedCount":result2["cn_jwsrNum"]
        # }
        return json_response(all_data)
class StatisticsView(APIView):
    def get(self,request):
        result = {}
        result2 = {}
        #需求：获取12月18号的中国的数据和世界的数据
        res_world =  models.WorldCov.objects.filter(date="2022.12.20").first()
        for field in models.WorldCov._meta.fields:
            name = field.attname
            value = getattr(res_world, name)
            result[name] = value
        all_data = {
            "confirmedCount":result["certain"],
            "confirmedIncr":result["die_inc"],
            "curedCount":result["recure"],
            "curedIncr":0,
            "deadCount":result["die"],
        }
        return json_response(all_data)
 

#获取到世界所有数据
class StatisticsListView(APIView):
    # 获取全部数据
    def get_China_obj(self):
        result = []
        values_fields = (
            'cn_jwsrNum', 'cn_heconNum',
            'cn_conNum', 'cn_deathNum', 'cn_cureNum',"cn_addjwsrNum","cn_province_econNum","cn_contactNum","ymd")
        res =  models.ChinaCov.objects.all().order_by("ymd")
        for item in res.values_list(*values_fields):
            item = dict(zip(values_fields, item))
            statistics = {}
            for name, value in item.items():
                print(name, value)
                statistics[name] = value
            result.append(statistics)
        result = result[::-1]
        return result

    def get_World_obj(self):
        result = []
        values_fields = (
            'die', 'certain',
            'recure', 'die_inc', 'recure_inc',"certain_inc","date")
        res =  models.WorldCov.objects.all().order_by("date")
        for item in res.values_list(*values_fields):
            item = dict(zip(values_fields, item))
            statistics = {}
            for name, value in item.items():
                print(name, value)
                statistics[name] = value
            result.append(statistics)
        result = result[::-1]
        return result
    def get(self,request): 
        result = []
        values_fields = (
            'die', 'certain',
            'recure', 'die_inc', 'recure_inc',"certain_inc","date")
        res =  models.WorldCov.objects.all().order_by("date")
        for item in res.values_list(*values_fields):
            item = dict(zip(values_fields, item))
            statistics = {}
            for name, value in item.items():
                print(name, value)
                statistics[name] = value
            result.append(statistics)
        result = result[::-1]
        return json_response(result)
class CountryRankView(APIView):
    def get(self,request):
        result = []
        values_fields = models.CountryCov.json_field
        res =  models.CountryCov.objects.all().order_by("conNum")
        for item in res.values_list(*values_fields):
            item = dict(zip(values_fields, item))
            statistics = {}
            for name, value in item.items():
                statistics[name] = value
            result.append(statistics)
        result = result[::-1]
        result2 = []
        print(result)

        for item in result:
            obj = {}
            obj["provinceLabel"] = item["name"]
            obj["confirmedCount"] = item["conNum"]
            obj["conadd"] = item["conadd"]
            obj["deadCount"] = item["deathNum"]
            obj["curedCount"] =  item["cureNum"]
            result2.append(obj)
        return json_response(result2)
class ProvinceView(APIView):
    def get(self,request):
        result = []
        values_fields = models.ProvinceCov.json_field
        res =  models.ProvinceCov.objects.all().order_by("value")
        for item in res.values_list(*values_fields):
            item = dict(zip(values_fields, item))
            statistics = {}
            for name, value in item.items():
                statistics[name] = value
            result.append(statistics)
        result2 = []
        for item in result:
            obj = {}
            obj["countryLabel"] = "中国"
            obj["countryName"] = "China"
            obj["provinceLabel"] = item["name"]
            obj["deadCount"] = item["deathNum"]
            obj["jwsrNum"] = item["jwsrNum"]
            obj["currentConfirmedCount"] = item["econNum"]
            obj["confirmedCount"] = item["value"]
            result2.append(obj)
        # for item in result:
        #     obj = {}
        #     obj["provinceName"] = item["name"]
        #     obj["deadCount"] = item["deathNum"]
        #     obj["jwsrNum"] = item["jwsrNum"]
        #     obj["currentConfirmedCount"] = item["econNum"]
        #     obj["confirmedCount"] = item["value"]
        #     result2.append(obj)
        result2 = result2[::-1]
        return json_response(result2)
class ChinaTrendView(APIView):
    def get_ChinaCov_obj(self):
        result = []
        values_fields = models.ChinaCov.json_field
        res =  models.ChinaCov.objects.all().order_by("ymd")
        for item in res.values_list(*values_fields):
            item = dict(zip(values_fields, item))
            statistics = {}
            for name, value in item.items():
                statistics[name] = value
            result.append(statistics)
        result = result[::-1]
        return result
    def get(self,request):
        obj = {
            "confirmedCountList":[],
            "curedCountList":[],
            "currentConfirmedCountList":[],
            "importedCountList":[],
            "importedIncrList":[],
            "currentConfirmedIncrList":[]
        }
        result = self.get_ChinaCov_obj()
        for item in result:
            item["ymd"] = item["ymd"].split(".")
            item["ymd"] = item["ymd"][1]+"-"+item["ymd"][2]
            obj["confirmedCountList"].append([item["cn_conNum"],item["ymd"]])
            obj["curedCountList"].append([item["cn_cureNum"],item["ymd"]])
            obj["currentConfirmedCountList"].append([item["cn_conNum"],item["ymd"]])
            obj["importedCountList"].append([item["cn_jwsrNum"],item["ymd"]])
            obj["importedIncrList"].append([item["cn_addjwsrNum"],item["ymd"]])
            obj["currentConfirmedIncrList"].append([item["cn_contactNum"],item["ymd"]])

        return json_response(obj)
