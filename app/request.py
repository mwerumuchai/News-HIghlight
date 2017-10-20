from app import app
import urllib.request,json
from .models import news

News = news.News

#Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the news base url
base_url = app.config['NEWS_API_BASE_URL']

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


		news_object = News(id,name,description,url,category)
		news_results.append(news_object)

	return news_results
