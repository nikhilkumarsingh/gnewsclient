import json
import requests
from bs4 import BeautifulSoup
from .utils import editionMap, topicMap, langMap
from newspaper import Article


class gnewsclient:
    
    def __init__(self, edition = 'United States (English)',
                 topic = 'top stories', location = None,
                 query = None, language = 'english'):
        '''
        constructor function
        '''
        # list of editions and topics
        self.editions = list(editionMap)
        self.topics = list(topicMap)
        self.languages = list(langMap)
        
        # default parameter values
        self.edition = edition
        self.topic = topic
        self.location = location
        self.query = query
        self.language = language
        
        # parameters to be passed in HTTP request
        self.params = {'output': 'atom',
                       'ned': self.edition,
                       'topic': self.topic,
                       'geo': self.location,
                       'q': self.query,
                       'hl': self.language}
            
    
    def get_config(self):
        '''
        function to get current configuration
        '''
        config = {
            'edition': self.edition,
            'topic': self.topic,
            'language': self.language,
            'loaction': self.location,
            'query': self.query
        }
        return config

    def reset(self):
        '''
        function to reset the parameters
        '''
        self.edition = 'United States (English)'
        self.language = 'english'
        self.location = None
        self.query = None
        self.topic = 'top stories'
            
            
    def get_news(self):
        '''
        function to fetch news articles
        '''
        status = self.set_params()
        # params not set properly
        if status == False:
            return

        soup = self.load_feed()
        articles = self.scrape_feed(soup)
        object_list = []
        for a in articles:
            #article = {}
            a['object'] = Article(a['link'])
        return articles

    def get_fulltext(self, article_obj):
        article_obj.download()
        article_obj.parse()
        return article_obj.text

    def get_metadata(self,article_obj):
        article_obj.download()
        article_obj.parse()
        metadata = {}
        metadata['date'] = article_obj.publish_date
        metadata['image'] = article_obj.top_image
        metadata['authors'] = article_obj.authors
        return metadata
    def get_summary(self, article_obj):
        article_obj.download()
        article_obj.parse()
        article_obj.nlp()
        return article_obj.summary

    
    def set_params(self):
        '''
        function to set params for HTTP request
        '''
        
        # setting edition
        try:
            self.params['ned'] = editionMap[self.edition]
        except KeyError:
            print("{} edition not found.\nUse editions attribute to get list of editions.".format(self.edition))
            return False
            
        # setting topic
        try:
            self.params['topic'] = topicMap[self.topic]
        except KeyError:
            print("{} topic not found.\nUse topics attribute to get list of topics.".format(self.topic))
            return False
        
        # setting language
        try:
            self.params['hl'] = langMap[self.language]
        except KeyError:
            print("{} language not found.\nUse langugaes attribute to get list of languages.".format(self.language))
            return False
            
        # setting query
        if self.query != None:
            self.params['q'] = self.query
            # topic overrides query parameter. So, clearing it.
            self.params['topic'] = None
            
        # setting location
        if self.location != None:
            self.params['geo'] = self.location
            # topic overrides location parameter. So, overriding it.
            self.params['topic'] = None

        # params setting successful
        return True
        
    
    def load_feed(self):
        '''
        function to load atom feed
        '''
        url = "https://news.google.com/news"
        resp = requests.get(url, params = self.params)
        soup = BeautifulSoup(resp.content, 'html5lib')
        return soup
    
    
    def scrape_feed(self, soup):
        '''
        function to scrape atom feed
        '''
        entries = soup.findAll('entry')
        articles = []

        for entry in entries:
            article = {}
            article['title'] = entry.title.text
            article['link'] = entry.link['href'].split('&url=')[1]
            articles.append(article)
        return articles       
