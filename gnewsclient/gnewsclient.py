import argparse

import feedparser
import requests
from fuzzywuzzy import process

from .PyOpenGraph import PyOpenGraph
from .utils import locationMap, langMap, topicMap, top_news_url, topic_url


class NewsClient:

    def __init__(self, location='United States', language='english', topic='Top Stories',
                 use_opengraph=False, max_results=10):
        """
        client initialization
        """
        # list of available locations, languages and topics
        self.locations = list(locationMap)
        self.languages = list(langMap)
        self.topics = list(topicMap)

        # setting initial configuration
        self.location = location
        self.language = language
        self.topic = topic

        # other settings
        self.use_opengraph = use_opengraph
        self.max_results = max_results

    def get_config(self):
        """
        function to get current configuration
        """
        config = {
            'location': self.location,
            'language': self.language,
            'topic': self.topic,
        }
        return config

    @property
    def params_dict(self):
        """
        function to get params dict for HTTP request
        """
        location_code = 'US'
        language_code = 'en'
        if len(self.location):
            location_code = locationMap[process.extractOne(self.location, self.locations)[0]]
        if len(self.language):
            language_code = langMap[process.extractOne(self.language, self.languages)[0]]
        params = {
            'hl': language_code,
            'gl': location_code,
            'ceid': '{}:{}'.format(location_code, language_code)
        }
        return params

    def get_news(self):
        """
        function to get news articles
        """
        if self.topic is None or self.topic == 'Top Stories':
            resp = requests.get(top_news_url, params=self.params_dict)
        else:
            topic_code = topicMap[process.extractOne(self.topic, self.topics)[0]]
            resp = requests.get(topic_url.format(topic_code), params=self.params_dict)
        return self.parse_feed(resp.content)

    def print_news(self):
        articles = self.get_news()
        for article in articles:
            print(article['title'])
            print(article['link'], end='\n\n')

    def parse_feed(self, content):
        """
        utility function to parse feed
        """
        feed = feedparser.parse(content)
        articles = []
        for entry in feed['entries'][:self.max_results]:
            article = {
                'title': entry['title'],
                'link': entry['link']
            }
            try:
                article['media'] = entry['media_content'][0]['url']
            except KeyError:
                article['media'] = None
            if self.use_opengraph:
                article = {**PyOpenGraph(article['link']).properties, **article}
            articles.append(article)
        return articles


def main():
    parser = argparse.ArgumentParser(description="GoogleNews Client CLI!")

    parser.add_argument("-loc", "--location", type=str, default='United States',
                        help="Set news location.")

    parser.add_argument("-lang", "--language", type=str, default='english',
                        help="Set news language.")

    parser.add_argument("-t", "--topic", type=str, default='Top Stories',
                        help="Set news topic.")

    parser.add_argument("-sloc", "--show-locations", action='store_true',
                        help="Show location choices")

    parser.add_argument("-slang", "--show-languages", action='store_true',
                        help="Show language choices")

    parser.add_argument("-st", "--show-topics", action='store_true',
                        help="Show topic choices")

    args = parser.parse_args()
    args_dict = vars(args)

    if args_dict['show_locations']:
        print("\n".join(locationMap.keys()))

    elif args_dict['show_languages']:
        print("\n".join(langMap.keys()))

    elif args_dict['show_topics']:
        print("\n".join(topicMap.keys()))

    client = NewsClient(location=args_dict['location'], language=args_dict['language'], topic=args_dict['topic'])
    client.print_news()


if __name__ == "__main__":
    main()
