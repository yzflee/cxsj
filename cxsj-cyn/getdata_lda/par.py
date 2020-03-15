from urllib.request import urlopen
from bs4 import BeautifulSoup

links=['']

def get_all_issue(url):
    html=urlopen(url)
    bso=BeautifulSoup(html,"html.parser")
    for link in bso.findAll("body"):

            print(link.attrs["body"])
            links.append(link.attrs["body"])


get_all_issue("https://api.github.com/repos/tensorflow/tensorflow/issues")
print(links)
print(links)
