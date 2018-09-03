# -*- coding: utf-8 -*-
import scrapy
import re
import json
import time
from ganji.items import GanjiItem
from ganji.cityList import cityList


class PersonFangSpider(scrapy.Spider):
    name = 'person_fang'

    def __init__(self, city=None,*args, **kwargs):
        super(PersonFangSpider, self).__init__(*args, **kwargs)
        self.city = city
        self.nowTime = time.time()

    def start_requests(self):
        city_code = cityList[self.city]
        jsonp = -2
        page_no = 1
        while page_no < 200:
            url = "http://fangapi.ganji.com/api/v1/fang/v1/post/houselist/?callback=jsonp{}&validListType=12,4&domain={}&url=fang1&agent=1&zufang=1&page=1&uri=a1m1%2F&a=pl&d=a1m1%2F&subway=false&category=fang1&city_domain={}&type=extend&page_no={}".format(jsonp,city_code,city_code,page_no)
            jsonp += 2
            page_no +=1
            yield scrapy.Request(url, dont_filter = True)


    def parse(self, response):
        item = GanjiItem()
        text = response.body.decode("utf-8")
        # try:
        data = re.sub(r'^json.*?\(','',text)
        data = re.sub(r'\)$','',data)
        data_json = json.loads(data)
        infos = data_json["data"]
        for info in infos:
            postTime = info["post_at"]
            timeArray = time.localtime(int(postTime))
            if self.nowTime-int(postTime)>86400*30:
                continue
            else:
                # title = info["title"]
                shopUrl ="http://{}.ganji.com/fang1/".format(cityList[self.city]) + info["puid"] +"x.htm"
                phone = info["phone"]
                cname = info["person"]

                item["phone"] = phone
                item["cname"] = cname
                item["postTime"] = time.strftime("%Y-%m-%d", timeArray)
                item["shopUrl"] = shopUrl
                # item["title"] = title
                item["city"] = self.city
                yield item


        # except Exception as e:
        #     print("空",e)
