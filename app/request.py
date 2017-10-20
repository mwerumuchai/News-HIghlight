from app import app
import urllib.request,json
from .models import news

News = news.News

#Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the news base url
base_url = app.config['NEWS_API_BASE_URL']

def get_news_source(category):
    '''
    Functions that gets the json response to out urllib
    '''
    get_news_source_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_source_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)


    return news_results

#processing results
def process_results(news_list):
    '''
    Functions that processes the movie result. Also transforms them to a list of objects

    Args:
        news_list: a list of dictionaries that contain movie details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')

    return news_results
