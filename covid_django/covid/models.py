from django.db import models
# from django.utils.translation import ugettext_lazy as _
class ChinaCov(models.Model):
    json_field = ('cn_jwsrNum','cn_heconNum','cn_conNum',
    'cn_deathNum','cn_cureNum','cn_addjwsrNum','cn_province_econNum',
    'cn_contactNum','ymd'
    )
    #累计境外输入
    cn_jwsrNum = models.IntegerField(  'cn_jwsrNum', default=0)
    #现存重症
    cn_heconNum = models.IntegerField(  'cn_heconNum', default=0)
    #累计确诊
    cn_conNum = models.IntegerField(  'cn_conNum', default=0)
    #累计死亡
    cn_deathNum = models.IntegerField(  'cn_deathNum', default=0)
    #累计治愈
    cn_cureNum = models.IntegerField(  'cn_cureNum', default=0)
    # 新增境外输入
    cn_addjwsrNum = models.IntegerField(  'cn_addjwsrNum', default=0)
    #现存本土确诊
    cn_province_econNum = models.IntegerField(  'cn_province_econNum', default=0)  
    #新增确诊
    cn_contactNum =  models.IntegerField(  'cn_contactNum', default=0) 
    #日期
    ymd = models.CharField(  'ymd', max_length=100,primary_key=True)
    class Meta:
        verbose_name =   'ChinaCov'
        verbose_name_plural =   'ChinaCov'
class WorldCov(models.Model):
    json_field = ("die","certain","recure","die_inc","recure_inc","certain_inc","certain_inc")
    #全球死亡总数
    die = models.IntegerField(  'die', default=0)
    #累计确诊
    certain = models.IntegerField(  'certain', default=0)
    #累计治愈
    recure = models.IntegerField(  'recure', default=0)
    #新增死亡
    die_inc = models.IntegerField(  'die_inc', default=0)
    # 新增治愈
    recure_inc =  models.IntegerField(  'recure_inc', default=0)
    # 新增确诊    
    certain_inc = models.IntegerField(  'certain_inc', default=0)
    #日期
    date = models.CharField(  'ymd', max_length=100,primary_key=True)
    class Meta:
        verbose_name =   'WorldCov'
        verbose_name_plural =   'WorldCov'
class CountryCov(models.Model):
    json_field = ("conNum","conadd","cureNum","deathNum","name")
    #     conNum =scrapy.Field() #确诊
    # conadd = scrapy.Field() #新增
    # cureNum = scrapy.Field() #治愈
    # deathNum = scrapy.Field() #死亡
    # name = scrapy.Field() #国家名字
    conNum = models.IntegerField(  'conNum', default=0)
    conadd = models.IntegerField(  'conadd', default=0)
    cureNum = models.IntegerField(  'cureNum', default=0)
    deathNum = models.IntegerField(  'deathNum', default=0)
    name = models.CharField(  'name', max_length=100,primary_key=True)
    class Meta:
        verbose_name =   'CountryCov'
        verbose_name_plural =   'CountryCov'
class ProvinceCov(models.Model):
    json_field = ("cureNum","deathNum","deathNum","econNum","jwsrNum","value","name")
    cureNum = models.IntegerField(  'cureNum', default=0)
    deathNum =  models.IntegerField(  'deathNum', default=0)
    econNum =  models.IntegerField(  'econNum', default=0)
    jwsrNum = models.IntegerField(  'jwsrNum', default=0)
    value = models.IntegerField(  'value', default=0)
    name = models.CharField(  'name', max_length=100,primary_key=True)
    class Meta:
        verbose_name =   'ProvinceCov'
        verbose_name_plural =   'ProvinceCov'