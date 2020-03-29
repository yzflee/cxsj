#-*- coding: utf-8 -*-

import requests

def get_banben_1():
    for i in range(400,500):
        url = 'https://api.github.com/repos/tensorflow/tensorflow/issues/37%s'%i
        content = requests.get(url).content.decode()
        with open('data/banben_1','a') as f:
            f.write(content)
    return