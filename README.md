[![PyPI](https://img.shields.io/badge/PyPi-v1.12-f39f37.svg)](https://pypi.python.org/pypi/gnewsclient)
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://github.com/nikhilkumarsingh/gnewsclient/blob/master/LICENSE.txt)

# gnewsclient

An easy-to-use python client for [Google News feeds](https://news.google.com/).

## Installation

To install gnewsclient, simply,
```
$ pip install gnewsclient
```

## Usage

- Create a NewsClient object:
    ```python
    >>> from gnewsclient import gnewsclient
    >>> client = gnewsclient.NewsClient(language='hindi', location='india', topic='Business', max_results=3)
    ```

- Get current parameter settings
    ```python
    >>> client.get_config()
    {'location': 'india', 'language': 'hindi', 'topic': 'Sorts'}
    ```

- Get news feed
    ```python
    >>> client.get_news()
    [{'title': 'शेयर बाजार/ सेंसेक्स 490 अंक की बढ़त के साथ 39055 पर, निफ्टी 150 प्वाइंट ऊपर 11726 पर बंद - दैनिक भास्कर',
      'link': 'https://www.bhaskar.com/national/news/stock-market-sensex-jumps-500-points-nifty-up-150-points-on-wednesday-24-april-01529551.html',
      'media': None},
     {'title': 'Reliance Jio की सेवाएं हो सकती हैं महंगी! यह है वजह - Jansatta',
      'link': 'https://www.jansatta.com/business/reliance-jio-planning-to-hike-in-prices-to-invest-9000-crore-in-capacity-lease-deals/990616/',
      'media': None},
     {'title': 'डील/ एस्सेल प्रोपैक की कंट्रोलिंग हिस्सेदारी 3211 करोड़ रुपए में खरीदेगी ब्लैकस्टोन - दैनिक भास्कर',
      'link': 'https://www.bhaskar.com/national/news/blackstone-snaps-up-essel-propack-for-rs-3211-cr-01528505.html',
      'media': 'https://lh3.googleusercontent.com/proxy/XgI0fJc8QD0syNzTzYgSyerob_9QSyKEIKZAdGecQ-C4u5HxjqcW-HrpuglbWj8CoxLDcrxOzT7QS7GNJxGv6kt6cviIzKpsaGpsr4qEwpyc=-w150-h150-c'},
     {'title': 'मारुति सुजुकी की बलेनो हुई स्मार्ट, जानें कीमत और खास फीचर्स - Hindustan',
      'link': 'https://www.livehindustan.com/business/story-maruti-suzuki-launched-new-smart-baleno-know-price-and-features-2500723.html',
      'media': 'https://lh6.googleusercontent.com/proxy/Jwm-p9YBF5bT3bcsXv5KGn_83nniRJsi9CArg1yU27LrKMu72cl1ekX4na_e9JfjhWHrRKD-LWLdUiK1H91VnB_gwVhoJNQX_AvhLaKUId-uodvOMDIe=-w150-h150-c'}]    
    ```
    
- Get news feed with OpenGraph data
    ```python
    >>> client = gnewsclient.NewsClient(language='hindi', location='india', topic='Business', use_opengraph=True, max_results=5)
    [{'url': 'https://aajtak.intoday.in/story/share-market-low-sensex-nifty-bse-nse-yesbank-ntpc-heromotoco-rupee-tut-1-1090122.html',
      'site_name': 'aajtak.intoday.in',
      'title': 'लाल निशान पर बंद हुआ शेयर बाजार, अब भी 40 हजार के पार - आज तक',
      'description': 'सप्ताह के दूसरे कारोबारी दिन भारतीय शेयर बाजार ने एक मुकाम को हासिल किया. हालांकि कारोबार के अंत में सेंसेक्स और निफ्टी लाल निशान पर बंद हुए.',
      'image': 'https://smedia2.intoday.in/aajtak/images/stories/062019/sensex_1559643004_618x347.jpeg',
      'type': 'Article',
      'image_width': 150,
      'image_height': 150,
      'link': 'https://aajtak.intoday.in/story/share-market-low-sensex-nifty-bse-nse-yesbank-ntpc-heromotoco-rupee-tut-1-1090122.html',
      'media': None},
     {'url': 'https://www.amarujala.com/photo-gallery/automobiles/bajaj-platina-110-h-gear-vs-tvs-victor-full-comparison-and-price',
      'site_name': 'Amar Ujala',
      'title': 'Bajaj Platina 110 Vs TVS Victor, जानिये कौन सी बाइक है वैल्यू फॉर मनी - अमर उजाला',
      'description': 'बजाज ऑटो ने भारत में अपनी नई Platina 110 H-Gear को लांच कर दिया है। नई Platina 110 का सीधा मुकाबला TVS की Victor से होगा। चाइये जानते हैं इन दोनों',
      'image': 'https://spiderimg.amarujala.com/assets/images/2019/06/05/750x506/bajaj-platina-110-vs-tvs-victor_1559719613.jpeg',
      'locale': 'hi_IN',
      'type': 'article',
      'headline': 'Bajaj Platina 110 H-Gear 110 या TVS Victor, जानिये कौन सी बाइक है सबसे बेहतर',
      'image_width': 150,
      'image_height': 101.19999999999999,
      'link': 'https://www.amarujala.com/photo-gallery/automobiles/bajaj-platina-110-h-gear-vs-tvs-victor-full-comparison-and-price',
      'media': None}]
    ```

- Changing parameters
    ```python
    >>> client.location = 'india'
    >>> client.language = 'hindi'
    >>> client.topic = 'Sports'
    >>> client.get_news()
    [{'title': 'जब डिविलियर्स ने एक हाथ से मारा शॉट, ग्राउंड के पार पहुंची गेंद - आज तक',
      'link': 'https://aajtak.intoday.in/sports/story/rcb-vs-kxip-ab-de-villiers-one-handed-six-out-of-the-ground-tspo-1-1078680.html',
      'media': None},
     {'title': 'हितों का टकराव: बीसीसीआई लोकपाल ने सचिन तेंडुलकर और वीवीएस लक्ष्मण को नोटिस जारी किया - Navbharat Times',
      'link': 'https://navbharattimes.indiatimes.com/sports/cricket/iplt20/news/ombudsman-notice-to-sachin-tendulkar-vvs-laxman-cricketers-doing-voluntary-service/articleshow/69031167.cms',
      'media': None},
     {'title': 'आंद्रे रसेल और गेल को मिला आईपीएल का ईनाम, वेस्टइंडीज की विश्वकप 2019 टीम में मिली जगह - India TV हिंदी',
      'link': 'https://hindi.indiatvnews.com/sports/cricket-world-cup-2019-westindies-team-squad-2019-chris-gayle-and-andre-russell-got-place-633917',
      'media': None},
     {'title': 'Macth Update, IPL 2019, RCB vs KXIP: पंजाब को हराकर बैंगलोर ने लगाई जीत की हैट्रिक, प्लेऑफ की दौड़ में बरकरार - Times Now Hindi',
      'link': 'https://hindi.timesnownews.com/cricket/article/ipl-live-score-rcb-vs-kxip-royal-challengers-bangalore-vs-kings-xi-punjab-m-chinnaswamy-stadium-ipl-2019-live-match-score-in-hindi/406206',
      'media': None}
    ]
    ```

- Get list of available locations, languages and topics
    ```python
    >>> client.locations
    ['Australia', 'Botswana', 'Canada ', 'Ethiopia', 'Ghana', 'India ', 'Indonesia', 'Ireland', 'Israel ', 'Kenya', 'Latvia',
     'Malaysia', 'Namibia', 'New Zealand', 'Nigeria', 'Pakistan', 'Philippines', 'Singapore', 'South Africa', 'Tanzania', 'Uganda', 
     'United Kingdom', 'United States', 'Zimbabwe', 'Czech Republic', 'Germany', 'Austria', 'Switzerland', 'Argentina', 'Chile',
     'Colombia', 'Cuba', 'Mexico', 'Peru', 'Venezuela', 'Belgium ', 'France', 'Morocco', 'Senegal', 'Italy', 'Lithuania', 
     'Hungary', 'Netherlands', 'Norway', 'Poland', 'Brazil', 'Portugal', 'Romania', 'Slovakia', 'Slovenia', 'Sweden', 'Vietnam',
     'Turkey', 'Greece', 'Bulgaria', 'Russia', 'Ukraine ', 'Serbia', 'United Arab Emirates', 'Saudi Arabia', 'Lebanon', 'Egypt',
     'Bangladesh', 'Thailand', 'China', 'Taiwan', 'Hong Kong', 'Japan', 'Republic of Korea']
    >>> client.languages
    ['english', 'indonesian', 'czech', 'german', 'spanish', 'french', 'italian', 'latvian', 'lithuanian', 'hungarian', 'dutch', 
    'norwegian', 'polish', 'portuguese brasil', 'portuguese portugal', 'romanian', 'slovak', 'slovenian', 'swedish', 'vietnamese', 
    'turkish', 'greek', 'bulgarian', 'russian', 'serbian', 'ukrainian', 'hebrew', 'arabic', 'marathi', 'hindi', 'bengali', 'tamil', 
    'telugu', 'malyalam', 'thai', 'chinese simplified', 'chinese traditional', 'japanese', 'korean']
    >>> client.topics
    ['Top Stories',
     'World',
     'Nation',
     'Business',
     'Technology',
     'Entertainment',
     'Sports',
     'Science',
     'Health']
    ```