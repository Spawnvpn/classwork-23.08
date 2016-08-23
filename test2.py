from urllib.request import urlopen
from bs4 import BeautifulSoup
from lxml import etree


def parce():
    a = urlopen('http://python.org')
    content = a.read()
    data_dict = dict()
    data_list = list()
    root = etree.HTML(content)
    bs = BeautifulSoup(content, 'html.parser')
    # return bs.find_all('p')
    # return bs.find_all('div', attrs={'class': 'shrubbery'})
    # return bs.find('div', attrs={'class': 'shrubbery'}).prettify()
    # return root.xpath('//a')[0].text
    # return root.xpath('//a')[0].attrib
    data = root.xpath('//div[contains(@class, "blog-widget")]/div/ul/li')
    for item in data:
        data_dict['time'] = item.xpath('.//time')[0].attrib['datetime']
        data_dict['link'] = item.xpath('.//a')[0].attrib['href']
        data_dict['link_text'] = item.xpath('.//a')[0].text
        data_list.append(data_dict)
    return data_list

print(parce())