from app import app
import urllib.request,json
from .models import news
# ,Article

News = news.News


#Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the news base url
base_url = app.config['NEWS_API_BASE_URL']
articles_base_url = app.config['NEWS_ARTICLES_BASE_URL']

def get_news_source(category):
	"""
	function that gets the json reponse to our url request
	"""
	get_news_url = base_url.format(category,api_key)

	with urllib.request.urlopen(get_news_url) as url:
		get_news_data = url.read()
		get_news_response = json.loads(get_news_data)

		news_results = None

		if get_news_response['sources']:
			news_results_list = get_news_response['sources']
			news_results = process_results(news_results_list)

	return news_results

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
	for source in news_list:
		id = source.get('id')
		name = source.get('name')
		description = source.get('description')
		url = source.get('url')
		category = source.get('category')


		news_source = News(id,name,description,url,category)
		news_results.append(news_source)

	return news_results

# #Articles section
# def get_articles(source):
# 	'''
# 	Function that gets the json response to our url request
# 	'''
# 	get_articles_url = articles_base_url.format(source,api_Key)
#
# 	with urllib.request.urlopen(get_articles_url) as url:
# 		get_articles_data = url.read()
# 		get_articles_response = json.loads(get_articles_data)
# 		articles_results = None
#
# 		if get_articles_response['articles']:
# 			articles_results_list = get_articles_response['articles']
# 			articles_results = process_articles(articles_results_list)
#
# 	return articles_results
#
# def process_articles(articles_results):
# 	'''
# 	Function  that processes the articles result and transform them to a list of Objects
# 	Args:
# 	    articles_results: A list of dictionaries that contain articles details
# 	Returns :
# 	    articles_list: A list of articles objects
# 	'''
# 	articles_list = []
# 	for article_item in articles_results:
# 		author = article_item.get('author')
# 		title = article_item.get('title')
# 		description = article_item.get('description')
# 		url = article_item.get('url')
# 		image = article_item.get('urlToImage')
# 		date = article_item.get('publishedAt')
#
# 		if date:
# 			article_object = Article(author,title,description,url,image,date)
# 			articles_list.append(article_object)
#
# 	return articles_list
