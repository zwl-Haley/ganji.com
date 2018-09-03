# -*- coding: utf-8 -*-
import scrapy
import re
import requests
from ganji.city_url_list import city_list
from ganji.items import GanjiItem
from selenium import webdriver
from lxml import etree

class GjSpider(scrapy.Spider):
    name = 'gj'

    # def __init__(self):
    #     pass

    def start_requests(self):
        for city_url in city_list:
            city_url = "http://3g.ganji.com" + city_url
            yield scrapy.Request(city_url)

    def parse(self, response):
        max_page = re.findall(r'class="page-num">1/(\d+)', response.text)[0]
        for page in range(1,int(max_page)+1):
            url = response.url.split("/?")[0] + "/o" + str(page) + "/"
            yield scrapy.Request(url, callback=self.parse_page)

    def parse_page(self, response):
        shop_urls = re.findall(r"""<a class="infor.*?href=['"](.*?)['"]""", response.text)
        location = re.findall(r'name="location" content="province=(.*?);city=(.*?);">', response.text)[0]
        for shop_url in shop_urls:
            shop_url = "https:" + shop_url
            yield scrapy.Request(shop_url, callback=self.parse_shop, meta={"location":location})

    def parse_shop(self, response):
        item = GanjiItem()
        province = response.meta["location"][0]
        city = response.meta["location"][1]
        category = "装修"
        title = re.findall(r'<div class="car-tit">(.*?)</div>', response.text)[0]
        if ".." in title:
            title = self.get_title(response.url)
        zhizhao = re.findall(r'营业执照已认证', response.text)
        if zhizhao:
            company = re.findall(r'([\u4e00-\u9fa5a-zA-Z0-9]+有限公司)', response.text)
            company = company[0] if company else self.get_company(response.url)
        else:
            company = ""
        cname = re.findall(r'<th>联系人</th>\n.*<td>(.*?)</td>', response.text)[0]
        phone = re.findall(r'>([0-9-]+)</span></a>',response.text)[0]
        service = re.findall(r'<i></i>(.*?)</a></li>', response.text)
        service = ",".join(service)
        address = re.findall(r'<th>店铺地址</th>\n.*?<td> (.*?) </td>', response.text)[0]
        if "wuba_info" in response.url:
            url1 = re.findall(r'https://3g.ganji.com/(.*?)/wuba_info/(\d+)/', response.url)[0]
            url = "http://{}.ganji.com/wuba_info/{}/".format(url1[0],url1[1])
        else:
            url1 = re.findall(r'https://3g.ganji.com/(.*?)/fuwu_dian/(\d+)x/\?', response.url)[0]
            url = "http://{}.ganji.com/fuwu_dian/{}x/".format(url1[0],url1[1])
        # shop_id = url.split("/")[-2]

        item["province"] = province
        item["city"] = city
        item["category"] = category
        item["title"] = title
        item["company"] = company
        item["cname"] = cname
        item["phone"] = phone
        item["service"] = service
        item["address"] = address
        item["url"] = url
        # item["shop_id"] = shop_id
        yield item


    def get_title(self, url):
        if "wuba_info" in url:
            url1 = re.findall(r'https://3g.ganji.com/(.*?)/wuba_info/(\d+)/', url)[0]
            url = "http://{}.ganji.com/wuba_info/{}/".format(url1[0],url1[1])
        else:
            url1 = re.findall(r'https://3g.ganji.com/(.*?)/fuwu_dian/(\d+)x/\?', url)[0]
            url = "http://{}.ganji.com/fuwu_dian/{}x/".format(url1[0],url1[1])
        r = requests.get(url, headers={"User-Agent":"Mozilla/5.0"})

        captcha = re.findall(r"请输入验证码",r.text)
        if captcha:
            with open("error.txt","a") as f:
                f.write(url+"\n")
            driver = webdriver.Chrome()
            driver.get("https://www.baidu.com")

        else:
            html = etree.HTML(r.text)
            title = html.xpath('//h1[@class="p1"]/text()')[0].replace("\n","").replace(" ","")
            return title

    def get_company(self, url):
        if "wuba_info" in url:
            url1 = re.findall(r'https://3g.ganji.com/(.*?)/wuba_info/(\d+)/', url)[0]
            url = "http://{}.ganji.com/wuba_info/{}/".format(url1[0],url1[1])
        else:
            url1 = re.findall(r'https://3g.ganji.com/(.*?)/fuwu_dian/(\d+)x/\?', url)[0]
            url = "http://{}.ganji.com/fuwu_dian/{}x/".format(url1[0],url1[1])
        r = requests.get(url+"contactus/", headers={"User-Agent":"Mozilla/5.0"})
        captcha = re.findall(r"请输入验证码",r.text)
        if captcha:
            with open("error.txt","a") as f:
                f.write(url+"\n")
            driver = webdriver.Chrome()
            driver.get("https://www.baidu.com")

        else:
            html = etree.HTML(r.text)
            company = html.xpath('//div[@class="fl"]/h1/text()')[0]
            return company