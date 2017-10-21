import urllib.request,json
from .models import Source, Article

#Getting api key
api_key = None



def configure_request(app):
	'''
    Function that takes in the application instance and Replaces the values of the None variables
    to application configuration objects
    '''
	global api_key,base_url
	api_key = app.config['NEWS_API_KEY']


def get_news_source(category):
	'''
	function that gets the json reponse to our url request
	'''
	get_news_url = 'https://newsapi.org/v1/sources'.format(category,api_key)

	with urllib.request.urlopen(get_news_url) as url:
		get_news_data = url.read()
		get_news_response = json.loads(get_news_data)

		news_results = None

		if get_news_response['sources']:
			source_results_list = get_news_response['sources']
			source_results = process_results(source_results_list)

	return source_results

#processing results
def process_results(news_list):
	"""
	function that processes news list dictonary and turns them to a list of objects

	Args:
		news_list: A list of dictonatires that contain news sources

	Return:
		new_results: A lists of news objects
	"""
	news_results = []
	for source_item in news_list:
		id = source_item.get('id')
		name = source_item.get('name')
		description = source_item.get('description')
		url = source_item.get('url')
		category = source_item.get('category')


		news_source = Source(id,name,description,url,category)
		news_results.append(news_source)

	return news_results

#Articles section
def get_articles_source(id):
	'''
	Function that gets the json response to our url request
	'''
	get_articles_url = 'https://newsapi.org/v1/articles?source={}&apiKey={}'.format(id,api_key)

	with urllib.request.urlopen(get_articles_url) as url:
		get_articles_data = url.read()
		get_articles_response = json.loads(get_articles_data)

		articles_results = None

		if get_articles_response['articles']:
			articles_results_list = get_articles_response['articles']
			articles_results = process_articles(articles_results_list)

	return articles_results

def process_articles(articles_list):
	'''
	Function  that processes the articles result and transform them to a list of Objects
	Args:
	    articles_list: A list of dictionaries that contain articles details
	Returns :
	    articles_results: A list of articles objects
	'''
	articles_results = []

	for article_item in articles_list:
		author = article_item.get('author')
		title = article_item.get('title')
		description = article_item.get('description')
		url = article_item.get('url')
		image = article_item.get('urlToImage')
		date = article_item.get('publishedAt')

		if date:
			article_object = Article(author,title,description,url,image,date)
			articles_results.append(article_object)

	return articles_results
