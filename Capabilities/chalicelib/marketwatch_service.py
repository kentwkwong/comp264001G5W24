from . import cloud_util as util
from bs4 import BeautifulSoup
import requests
import numpy as np
import re
import json
import sys
from contextlib import contextmanager

class MarketWatch:
    def __init__(self, stock_code):
        self.articles = []
        self.num_retrive = util.MAX_ARTICLES
        url = util.MARKETWATCH_URL.replace('@STOCKCODE',stock_code)
        headers = util.HEADER
        response = requests.get(url, headers=headers)
        self.soup = BeautifulSoup(response.text, 'html.parser')
    
    def get_article_urls(self):
        article_urls = []
        links = self.soup.find_all('a', {'class':'figure__image disableShadowBox'})
        for l in links:
            article_urls.append(l['href'])
        
        if self.num_retrive > len(article_urls):
            self.num_retrive = len(article_urls)
        return article_urls
    
    def get_articles(self):
        result = {}
        self.articles = []
        try:
            counter = 0
            regexp = re.compile(rf'{util.MARKETWATCH_SKIP_CONTENT}')
            for url in self.get_article_urls():
                print(f'DEBUG --> url: {url}')
                news_response = requests.get(url, headers=util.HEADER)
                news_soup = BeautifulSoup(news_response.text, 'html.parser')
                article_body = news_soup.find('div', {'class':{'article__body'}})
                if article_body == None:
                    # print('----->    NOT IN PATTERN!!')
                    continue
                news = article_body.find_all('p')

                content = ""
                for paragraph in news:
                    content += paragraph.text
                if not regexp.search(content):
                    # print(f'DEBUG --> real news: {url}')
                    self.articles.append({'url':url,'content':content})
                    counter += 1
                if counter >= self.num_retrive:
                    break

        except Exception as e:
            print(f'     ----- ERROR!! -----')
            print(e)
            print(f'------------------------')
        return self.articles