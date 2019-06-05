from html.parser import HTMLParser
from typing import Dict

import requests


class PyOpenGraph(object):

    def __init__(self, url):
        try:
            html = requests.get(url).text
        except:
            html = "<html></html>"
        p = PyOpenGraphParser()
        p.feed(html)

        if p.properties['image'] and p.properties['image:height'] and p.properties['image:width']:
            ratio = int(p.properties['image:height']) / int(p.properties['image:width'])
            p.properties['image_width'] = 150
            p.properties['image_height'] = 150 * ratio
        else:
            p.properties['image_width'] = 150
            p.properties['image_height'] = 150
        p.properties.pop('image:height', None)
        p.properties.pop('image:width', None)
        self.properties = p.properties
        p.close()

    def __str__(self):
        return self.properties['title']


class PyOpenGraphParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.properties = {'url': None, 'site_name': None, 'title': None, 'description': None,
                           'image': None, 'image:height': None, 'image:width': None}

    def handle_starttag(self, tag, attrs):
        if tag == 'meta':
            attrdict = dict(attrs)
            if 'property' in attrdict and attrdict['property'].startswith('og:') and 'content' in attrdict:
                self.properties[attrdict['property'].replace('og:', '')] = attrdict['content']

    def handle_endtag(self, tag):
        pass

    def error(self, msg):
        pass
