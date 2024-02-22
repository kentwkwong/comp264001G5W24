from . import cloud_util as util
from bs4 import BeautifulSoup
import requests
import numpy as np
import re
import json
import sys
from contextlib import contextmanager

class SeekingAlpha:
    def __init__(self, stock_code):
        self.stock_code = stock_code
        self.articles = []
        self.num_retrive = util.MAX_ARTICLES
        url = f'{util.SEEKINGALPHA_URL}/symbol/{stock_code}'
        headers = util.HEADER
        response = requests.get(url, headers=headers)
        self.soup = BeautifulSoup(response.text, 'html.parser')
    
    def get_article_urls(self):
        article_urls = []
        links = self.soup.find_all('a', {'data-test-id':'post-list-item-title'})
        for l in links:
            url = f"{util.SEEKINGALPHA_URL}{l['href']}"
            article_urls.append(url)
        
        if self.num_retrive > len(article_urls):
            self.num_retrive = len(article_urls)
        return article_urls
    
    def get_articles(self):
        self.articles = []
        try:
            counter = 0
            regexp = re.compile(rf'{util.SEEKINGALPHA_SKIP_CONTENT}')
            for url in self.get_article_urls():
                print(f'DEBUG --> url: {url}')
                # print(f'DEBUG --> -------------------------------')
                news_response = requests.get(url, headers=util.HEADER)
                ascii_content = news_response.text.encode('ascii','ignore').decode('ascii')
                news_soup = BeautifulSoup(ascii_content, 'html.parser')
                news = news_soup.find_all('p')
                content = ""
                for p in news:
                    paragraph = p.text
                    if not regexp.search(paragraph):
                        content += paragraph
                self.articles.append({'url':url, 'stockcode':self.stock_code,'content':content})
                counter += 1
                # print(content)
                # print(f'DEBUG --> -------------------------------')
                if counter >= self.num_retrive:
                    break
        except Exception as e:
            print(f'     ----- ERROR!! -----')
            print(e)
            print(f'------------------------')
        
        return self.articles