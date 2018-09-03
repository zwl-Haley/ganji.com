# -*- coding: utf-8 -*-
import scrapy
import re
import json,jsonpath
import time
from ganji.items import GanjiItem

class GjSpider(scrapy.Spider):
    name = 'gj'
    start_urls = ['https://3g.ganji.com/wh_housing/','https://3g.ganji.com/wh_housing/?b=sell']

    # jsonp = 
    # page_no = 
    # city =
    # fang =
    # uri = 
    # url = "http://fangapi.ganji.com/api/v1/fang/v1/post/houselist/?callback=jsonp{}&domain={}&url={}&uri={}&category={}&city_domain={}&page_no={}".format(str(jsonp),city,fang,uri,fang,city,str(page_no))
    # url = "http://fangapi.ganji.com/api/v1/fang/v1/post/houselist/?callback=jsonp-2&domain=wh&url=fang1&uri=a1m1%2F&category=fang1&city_domain=wh&page_no=1"

    def __init__(self):
        self.nowTime = time.time()

    def parse(self, response):
        jsonp = -2
        page_no = 1
        city = "wh"

        text = response.body.decode("utf-8")
        hrefs = re.findall(r'href="(/wh_fang.*?)"',text)
        for href in hrefs:
            fang = re.findall(r'_(fang.*?)/',href)[0]
            uri = re.findall(r'_fang.*?/(.*?)/',href)
            if uri:
                uri = uri[0]
            else:
                uri = ""
            while page_no < 150:
                url = "http://fangapi.ganji.com/api/v1/fang/v1/post/houselist/?callback=jsonp{}&domain={}&url={}&uri={}&category={}&city_domain={}&page_no={}".format(str(jsonp),city,fang,uri,fang,city,str(page_no))
                jsonp += 2
                page_no +=1
                yield scrapy.Request(url,callback=self.parse_info,dont_filter=True,meta={"fang":fang})

    def parse_info(self,response):
        item = GanjiItem()
        text = response.body.decode("utf-8")
        try:
            data = re.sub(r'^json.*?\(','',text)
            data = re.sub(r'\)$','',data)
            data_json = json.loads(data)
            infos = data_json["data"]
            for info in infos:
                postTime = info["post_at"]
                if self.nowTime-int(postTime)>86400*30:
                    continue
                else:
                    # title = info["title"]
                    # shopUrl ="http://wh.ganji.com/" + fang +"/" + info["puid"] +"x.htm"

                    phone = info["phone"]
                    cname = info["person"]

                    item["phone"] = phone
                    item["cname"] = cname
                    item["postTime"] = postTime
                    yield item


        except Exception as e:
            print("空",e)


