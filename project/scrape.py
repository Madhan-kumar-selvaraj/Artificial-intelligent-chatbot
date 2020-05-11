# -*- coding: utf-8 -*-
"""
Created on Sat May  9 22:59:57 2020

@author: Madhan Kumar Selvaraj
"""

import requests
from lxml import html

meta_data = "https://www.google.com/search?client=firefox-b-d&q="

def scrape_data(raw_text, text_type):
    input_type = text_type
    join_data = "<br /> &nbsp;"
    check_text = raw_text.split(" ")[-1]
    raw_text = raw_text.replace(" ","+")
    if check_text == "here" or check_text == "now" or text_type == "nearby":
        text_type = "" 
    raw_text = meta_data + raw_text + text_type
    text_type = input_type
    pageContent=requests.get(raw_text)
    tree = html.fromstring(pageContent.content)
    if check_text == "here" or check_text == "now":
        response = tree.xpath('.//div[@class="BNeawe iBp4i AP7Wnd"]/text()')[0]
    elif check_text == "link":
        response = tree.xpath('.//div[@class="X7NTVe"]//a/@href')[:6]
        response = response[::2]
        response = join_data.join(response)
    elif text_type == "nearby":
        response = tree.xpath('.//div[@class="BNeawe deIvCb AP7Wnd"]//text()')[1:4]
        response = join_data.join(response)
    else:
        response = tree.xpath(('.//div[@class="BNeawe s3v9rd AP7Wnd"]/text()'))[0]
    return response


