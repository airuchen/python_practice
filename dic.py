#!/usr/bin/python

from bs4 import BeautifulSoup as bs
import re
from requests import get

class dictionary:
    def __init__(self,word):
        self.word = word
        self.lookup()
    def remove_non_ascii(self,txt):
        return re.sub(r'[^\00-\x7f]+', '', txt)

    def get_soup(self,url):
        raw = self.remove_non_ascii(get(url).content)
        soup = bs(raw, "lxml")
        for i in range(0,10):
            print(soup.select("#MainTxt")[0].select('.ds-single')[i].text.strip())
            print('\n')
        #return soup.title.string

    def lookup(self):
        # base_url = "https://www.merriam-webster.com/dictionary/"
        base_url = "http://www.thefreedictionary.com/"
        query_url = base_url + self.word
        return self.get_soup(query_url)

dic = dictionary("read")
# print(dic.lookup("book"))

