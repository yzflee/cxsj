#-*- coding: utf-8 -*-

import requests
import os
import json

def get_banben():
    if os.path.isfile('data/banben_1.txt'):
        return
    for i in range(100,900):
        url = 'https://api.github.com/repos/tensorflow/tensorflow/issues/36%s'%i
        content = requests.get(url).content.decode()
        content = json.loads(content)
        with open('data/banben_1.txt','a+',encoding='utf-8') as f:
            f.write(content['body'])
        url2 = 'https://api.github.com/repos/tensorflow/tensorflow/issues/35%s'%i
        content2 = requests.get(url2).content.decode()
        content2 = json.loads(content2)
        with open('data/banben_2.txt','a+',encoding='utf-8') as f:
            f.write(content2['body'])
        url3 = 'https://api.github.com/repos/tensorflow/tensorflow/issues/32%s'%i
        content3 = requests.get(url3).content.decode()
        content3 = json.loads(content3)
        with open('data/banben_3.txt','a+',encoding='utf-8') as f:
            f.write(content3['body'])
        url4 = 'https://api.github.com/repos/tensorflow/tensorflow/issues/30%s'%i
        content4 = requests.get(url4).content.decode()
        content4 = json.loads(content4)
        with open('data/banben_4.txt','a+',encoding='utf-8') as f:
            f.write(content4['body'])
        url5 = 'https://api.github.com/repos/tensorflow/tensorflow/issues/29%s'%i
        content5 = requests.get(url5).content.decode()
        content5 = json.loads(content5)
        with open('data/banben_5.txt','a+',encoding='utf-8') as f:
            f.write(content5['body'])
        url6 = 'https://api.github.com/repos/tensorflow/tensorflow/issues/27%s' % i
        content6 = requests.get(url6).content.decode()
        content6 = json.loads(content6)
        with open('data/banben_6.txt', 'a+', encoding='utf-8') as f:
            f.write(content6['body'])
        url7 = 'https://api.github.com/repos/tensorflow/tensorflow/issues/25%s' % i
        content7 = requests.get(url7).content.decode()
        content7 = json.loads(content7)
        with open('data/banben_7.txt', 'a+', encoding='utf-8') as f:
            f.write(content7['body'])
        url8 = 'https://api.github.com/repos/tensorflow/tensorflow/issues/22%s' % i
        content8 = requests.get(url8).content.decode()
        content8 = json.loads(content8)
        with open('data/banben_8.txt', 'a+', encoding='utf-8') as f:
            f.write(content8['body'])
        url9 = 'https://api.github.com/repos/tensorflow/tensorflow/issues/20%s' % i
        content9 = requests.get(url9).content.decode()
        content9 = json.loads(content9)
        with open('data/banben_9.txt', 'a+', encoding='utf-8') as f:
            f.write(content9['body'])
        url10 = 'https://api.github.com/repos/tensorflow/tensorflow/issues/18%s' % i
        content10 = requests.get(url10).content.decode()
        content10 = json.loads(content10)
        with open('data/banben_10.txt', 'a+', encoding='utf-8') as f:
            f.write(content10['body'])
    return
get_banben()