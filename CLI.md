# gnews

CLI to use gnewsclient

How to use?
-----------

To use, it is recommended to make `virtualenv` and then install all required packages:

* Installing virtualenv:  
```
$ sudo pip install virtualenv
```  
* Making virtualenv:  
```
$ virtualenv venv
```  
* Go to your gnewsclient dir and activate it:   
```
$ . venv/bin/activate
```  
* To install all required packages:  
 ```
 $ pip install --editable .
 or
 $ sudo pip install --editable .
```


## Usage: `$ gnews [OPTIONS]`

```
Options:
  --config         shows default config
  --query TEXT     shows news about query given
  --edition TEXT   shows news of edition given, default=United States
                   (English)
  --topic TEXT     shows topic given, default=top stories
  --location TEXT  shows news from location given
  --language TEXT  shows news in language given, default is english
  --sheditions     shows list of available editions
  --shtopics       shows list of available topics
  --shlangs        shows list of available languages
  --help           Show this message and exit.

 ```