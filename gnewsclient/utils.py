import json
import pkg_resources

top_news_url = "https://news.google.com/news/rss"
topic_url = "https://news.google.com/news/rss/headlines/section/topic/{}"


def get_relative_path(filename):
    return pkg_resources.resource_filename(__name__, 'data/{}'.format(filename))


langMap = json.load(open(get_relative_path('langMap.json'), 'r'))
locationMap = json.load(open(get_relative_path('locationMap.json'), 'r'))
topicMap = json.load(open(get_relative_path('topicMap.json'), 'r'))
