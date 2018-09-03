# -*- coding: utf-8 -*-
from selenium import webdriver


def deal_captcha():
    browser = webdriver.Chrome()
    browser.get("https://callback.ganji.com/firewall/valid/1899567955.do?namespace=ganji_hy_detail_m")
    browser.maximize_window()
    while True:
        if not "callback" in browser.current_url:
            break
        else:
            pass
    browser.close()

deal_captcha()