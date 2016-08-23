from pyquery import PyQuery as pq
from urllib.request import urlopen
from bs4 import BeautifulSoup
from lxml import etree


def parce():
    a = urlopen('http://python.org')
    content = a.read()
    data_dict = dict()
    data_list = list()
    d = pq(content)
    d = d('.blog-widget div ul li')
    for item in d:
        item = pq(item)
        data_dict['time'] = item('time').attr('datetime')
        data_dict['link'] = item('a').attr('href')
        data_dict['link_text'] = item('a').text()
        data_list.append(data_dict)
    return data_list

print(parce())
