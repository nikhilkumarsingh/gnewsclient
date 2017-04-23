[![PyPI](https://img.shields.io/badge/PyPi-v1.0.2-f39f37.svg)](https://pypi.python.org/pypi/gnewsclient)
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://github.com/nikhilkumarsingh/gnewsclient/blob/master/LICENSE.txt)

# gnewsclient

An easy-to-use python client for [Google News feeds](https://news.google.com/).

gnewsclient supports Python 2 as well as Python 3.

## Installation

To install gnewsclient, simply,
```
$ pip install gnewsclient
```

## Filters

Google News feeds use 3 basic filters:

- **Edition**<br/>
    Limits results to a specific edition.<br/>
    There are more than 70 regional editions of Google News in many different languages. Each edition is specifically
    tailored with news for that audience.


- **Topic**<br/>
    Limits results to a specific topic.<br/>
    There are several custom topics like sports, business, world, health, science, politics, etc.


- **Location**<br/>
    Limits results to a specific location.

Other than these, you can also specify:

- **Language**<br/>
    Provides results in specified language.<br/>
    60+ languages are supported.
    
    
- **Query**<br/>
    Provide results according to a specific query.

## Usage

- Create a gnewsclient object:
```python
>>> from gnewsclient import gnewsclient
>>> client = gnewsclient()
```

- Get current parameter settings
```python
>>> client.get_config()
{'edition': 'United States (English)',
 'language': 'english',
 'loaction': None,
 'query': None,
 'topic': 'top stories'}
```

- Get news feed
```python
>>> client.get_news()
[{'img': 'https://t1.gstatic.com/images?q=tbn:ANd9GcQ5KFdYdQclmxUdvdV2zYQ_hO7JMrG2864ZDdN9A3GxORmTf_issciogLEEZmA5QIFfRQsyYDlm',
  'link': 'https://www.washingtonpost.com/world/french-citizens-vote-in-an-uncertain-race-that-could-determine-europes-future/2017/04/23/fd3759ce-1fa4-11e7-bb59-a74ccaf1d02f_story.html',
  'title': "French citizens vote in an uncertain race that could determine Europe's future - Washington Post"},
 {'img': 'https://t0.gstatic.com/images?q=tbn:ANd9GcTfosRmEfpoH40YiX5dyEIgL5rw-OSgcsKGEYhIm15f-OVQmWoidnH5NZD6P1vwaZfpQ33Xt8tZ',
  'link': 'https://www.washingtonpost.com/national/health-science/big-turnout-expected-for-march-for-science-in-dc/2017/04/21/67cf7f90-237f-11e7-bb9d-8cd6118e1409_story.html',
  'title': "Why people are marching for science: 'There is no Planet B' - Washington Post"},
 {'img': 'https://t2.gstatic.com/images?q=tbn:ANd9GcRw4xGtSrL5ZCpDkp5QHLUBPLgDNCsFFpgjJeOdD2q4w4giPDsDf9G3NOAZeNYWOf8f5V1aYTLu',
  'link': 'https://www.washingtonpost.com/politics/nearing-100-days-trumps-approval-at-record-lows-but-his-base-is-holding/2017/04/22/a513a466-26b4-11e7-b503-9d616bd5a305_story.html',
  'title': "Nearing 100 days, Trump's approval at record lows but his base is holding - Washington Post"}
]
```

- Changing paramteres
```python
>>> client.edition = 'India (Hindi)'
>>> client.topic = 'sports'
>>> client.language = 'hindi'
>>> client.get_news()
[{'img': 'https://t0.gstatic.com/images?q=tbn:ANd9GcTSo3cJx_-NKmtcsAaB8ZNC6tVF-FzU7FxLMmT9GwETYw-h_XmgzE_Ux2Bz3e2dk_iRUsaCIwbY',
  'link': 'http://aajtak.intoday.in/sports/story/ms-dhoni-is-the-captain-of-shane-warnes-all-time-ipl-eleven-1-925107.html',
  'title': 'वॉर्न की IPL टीम में भारतीयों का बोलबाला, धोनी को सौंपी कप्तानी - आज तक'},
 {'img': 'https://t1.gstatic.com/images?q=tbn:ANd9GcTlK3tT02bbryKfJS_l-fbICNHDUFsaXktMQSnvg_Pi-TWMBknuvBL3OhViOGzhjOcMtig4pg3t',
  'link': 'http://www.patrika.com/news/kanpur/jwala-gutta-says-up-government-should-make-strategy-for-better-sports-hindi-news-1560241/',
  'title': 'प्यार का करारनामा, इंटरनेशनल बैडमिंटन प्लेयर ज्वाला गुट्टा के हाथ पर नजर आया! - Patrika'}
]
```

- Get news by query
```python
>>> client.query = 'cricket'
>>> client.get_news()
[{'img': 'https://t2.gstatic.com/images?q=tbn:ANd9GcTQ6zOoooNhFaXM7bdl2WmmuJkHdE5ED26Mp2QtaRyKELMlBuvc62LmDVgt7-D3m7mgIPGI4vXf',
  'link': 'http://www.espncricinfo.com/west-indies-v-pakistan-2017/content/story/1094080.html',
  'title': 'West Indies v Pakistan, 1st Test, Kingston, 2nd day April 22, 2017 - ESPNcricinfo.com'},
 {'img': 'https://t1.gstatic.com/images?q=tbn:ANd9GcRePCUSgV_AXDrzSe59DsO7j6tgdcfWWocnusHc4OtLxNtGNloVuh_HPA1BtibucOTO9r-qwtNL',
  'link': 'https://thefield.scroll.in/835391/cricket-china-bowled-out-for-28-in-world-league-qualifier',
  'title': 'Cricket: China bowled out for 28 in World League qualifier - Scroll.in'},
 {'img': 'https://t2.gstatic.com/images?q=tbn:ANd9GcSpVMJHsdo6Q5SxuIzwrBHn7seXis3zwryH5ohRyeLVZj3phQDX1e92HZqW7iODBeJM7mrGf7yH',
  'link': 'http://www.hindustantimes.com/ipl-2017/live-cricket-score-ipl-2017-t20-mumbai-indians-vs-delhi-daredevils-live/story-CLQVOWa9v8ub7clUSz41LN.html',
  'title': 'Full Cricket Score, IPL 2017, T20, Mumbai Indians vs Delhi Daredevils: MI beat DD by 14 runs - Hindustan Times'}
]
```

- Get news by location
```python
>>> client.loaction = 'delhi'
>>> client.get_news()
[{'img': 'https://t3.gstatic.com/images?q=tbn:ANd9GcQI4mXbCB-bLvuiCqN1BoAyClMWgllzHy8DG9SCNDr3_dH9JpNpgfqTz8UneHeE85jdi0wknyhF',
  'link': 'http://timesofindia.indiatimes.com/city/delhi/cops-wrap-city-in-a-multi-layer-security-blanket/articleshow/58305944.cms',
  'title': 'MCD polls: Cops wrap Delhi in multi-layer security blanket - Times of India'},
 {'img': 'https://t0.gstatic.com/images?q=tbn:ANd9GcTd-gOZQ59kAj-GJ9uEHQ3wbGMF6Y4dI9pkc2B9RI0YyOrBPB4jIljR5zFFRXlB0KjqcuZxkAVl',
  'link': 'http://www.financialexpress.com/india-news/mcd-polls-2017-heritage-not-on-any-partys-agenda/637968/',
  'title': "MCD polls 2017: Heritage not on any party's agenda - Financial Express"},
 {'img': 'https://t1.gstatic.com/images?q=tbn:ANd9GcRK_YvCPtCF1uiA8aKz3LJLPHFP7zAlPHFkotuxL7Jr8DZBnA-w5HfMCe1Q69J7Cpf_AKKsNKeV',
  'link': 'http://timesofindia.indiatimes.com/city/delhi/car-owner-booked-for-kashmere-gate-accident/articleshow/58308236.cms',
  'title': 'Car owner booked for Kashmere Gate accident - Times of India - Times of India'}
]
```
- Get list of available editions, languages and topics
```python
>>> client.editions
['Germany', 'Poland', 'Morocco', 'Colombia', 'India (Telugu)', 'Australia', 'Hungary', 'India (Malayalam)', 
'United Arab Emirates', 'Lebanon', 'Serbia', 'Canada (English)', 'China', 'United States (English)', 
'Nigeria', 'Austria', 'Kenya', 'Peru', 'Italy', 'Ghana', 'Ukraine (Russian)', 'Belgium (French)', 'Vietnam', 
'South Africa', 'Ethiopia', 'Lithuania', 'Philippines', 'Brazil', 'Saudi Arabia', 'India (Hindi)', 'India (Tamil)',
'United States (Spanish)', 'Latvia', 'Singapore', 'Norway', 'Sweden', 'Canada (French)', 'Egypt', 'Japan', 
'Arab world', 'Ukraine (Ukranian)', 'Netherlands', 'Hong Kong', 'Romania', 'United Kingdom', 'Slovakia', 
'Czech Republic', 'Chile', 'Indonesia', 'France', 'Bangladesh', 'Taiwan', 'Tanzania', 'Argentina', 'Greece', 
'Mexico', 'Pakistan', 'Bulgaria', 'Senegal', 'Zimbabwe', 'Belgium (Dutch)', 'Uganda', 'Turkey', 'Portugal', 
'Slovenia', 'Namibia', 'Cuba', 'New Zealand', 'Russia', 'India (English)', 'Botswana', 'Venezuela', 'Israel (Hebrew)',
'Thailand', 'Switzerland', 'Israel (English)', 'Ireland', 'Malaysia']
>>> client.topics
['business', 'politics', 'top stories', 'technology', 'world', 'sports', 'entertainment', 'national']
>>> client.languages
['tamil', 'kannada', 'norwegian', 'swedish', 'bulgarian', 'arabic', 'hindi', 'catalan', 'georgian', 'latvian',
'albanian', 'japanese', 'english', 'german', 'lithuanian', 'chinese simplified', 'polish', 'czech', 'macedonian',
'yiddish', 'turkish', 'dutch', 'urdu', 'serbian', 'basque', 'thai', 'hungarian', 'danish', 'galician', 'latin', 
'chinese traditional', 'vietnamese', 'portuguese', 'welsh', 'croatian', 'bengali', 'finnish', 'icelandic', 
'azerbaijani', 'swahili', 'malay', 'korean', 'slovak', 'russian', 'irish', 'spanish', 'belarusian', 'french',
'estonian', 'indonesian', 'slovenian', 'italian', 'maltese', 'haitian creole', 'esperanto', 'ukrainian', 
'afrikaans', 'filipino', 'gujarati', 'hebrew', 'telugu', 'greek', 'persian', 'romanian']
```