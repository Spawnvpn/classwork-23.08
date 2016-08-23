from urllib.request import urlopen
from bs4 import BeautifulSoup


def parce():
    a = urlopen('http://python.org')
    content = a.read()
    bs = BeautifulSoup(content, 'html.parser')
    # return bs.find_all('p')
    # return bs.find_all('div', attrs={'class': 'shrubbery'})
    return bs.find('div', attrs={'class': 'shrubbery'}).prettify()


print(parce())
