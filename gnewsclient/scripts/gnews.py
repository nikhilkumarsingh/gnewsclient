import click
from gnewsclient import gnewsclient

client = gnewsclient()

@click.command()
@click.option("--config",is_flag=True,help="shows default config")

@click.option("--query",default=None,help="shows news about query given")
@click.option("--edition",default="United States (English)",help="shows news of edition given, default=United States (English)")
@click.option("--topic",default="top stories",help="shows topic given, default=top stories")
@click.option("--location",default=None,help="shows news from location given")
@click.option("--language",default="english",help="shows news in language given, default is english")

@click.option("--sheditions",is_flag=True,help="shows list of available editions")
@click.option("--shtopics",is_flag=True,help="shows list of available topics")
@click.option("--shlangs",is_flag=True,help="shows list of available languages")

def cli(config,query,edition,topic,location,language,shlangs,shtopics,sheditions):
	""" CLI to get news """

	client.query = query
	client.edition = edition
	client.topic = topic
	client.location = location
	client.language = language

	if config:
		conf = client.get_config()
		click.echo("The default configuration : ")
		for keys,value in conf.items():
			click.echo(str(keys)+" : "+str(value))

	elif shlangs:
		langs = client.languages
		click.echo("The languages supported : ")
		for l in langs:
			click.echo(l)

	elif sheditions:
		editions = client.editions
		click.echo("The editions available : ")
		for e in editions:
			click.echo(e)

	elif shtopics:
		tps = client.topics
		click.echo("The topics available : ")
		for t in tps:
			click.echo(t)
	else:
		neews = client.get_news()
		for n in neews:
			content = "{}\n{}".format(n['title'],n['link'])
			click.echo(content)
			click.echo("\n")