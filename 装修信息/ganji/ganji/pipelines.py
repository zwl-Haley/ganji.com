# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html



import pymysql
import datetime

class GanjiPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host = "127.0.0.1",
            port = 3306,
            db = "ganji",
            user = "root",
            passwd = "",
            charset = 'utf8',
            use_unicode = True
            )
        self.cursor = self.connect.cursor()
    print("连接数据库成功，正在存入数据库...")

    def process_item(self, item, spider):
        # sql = "SELECT phone FROM zhuangxiu WHERE phone = '{}';".format(item['phone'])
        # status = self.cursor.execute(sql)
        # if status == 0:
        self.cursor.execute(
            """replace into zhuangxiu(create_time, province, city, category, title, company, cname, phone, service, address, url)
            value (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
            (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            item["province"],
            item["city"],
            item["category"],
            item["title"],
            item["company"],
            item["cname"],
            item["phone"],
            item["service"],
            item["address"],
            item["url"]
            # item["shop_id"]
             ))
        self.connect.commit()
        # else:pass
        return item

    def close_spider(self,spider):
        self.connect.close()


# CREATE TABLE zhuangxiu (
#     auto_id INT NOT NULL primary key AUTO_INCREMENT,
#     create_time DateTime NOT NULL,
#     province VARCHAR(20),
#     city VARCHAR(20),
#     category VARCHAR(20),
#     title VARCHAR(100),
#     company VARCHAR(50),
#     cname VARCHAR(30),
#     phone VARCHAR(50),
#     service VARCHAR(200),
#     address VARCHAR(100),
#     url VARCHAR(100),
#     shop_id VARCHAR(20));