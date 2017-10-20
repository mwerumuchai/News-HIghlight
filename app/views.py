from flask import render_template
from app import app
from .request import get_news_source

#news
@app.route('/')
def index():
	"""
	new root page function return the page with all of its dat
	"""

	#getting general news
	general_news = get_news_source('general')
	entertainment_news = get_news_source('entertainment')
	technology_news =  get_news_source('technology')
	business_news = get_news_source('business')
	title = 'Home - News Highlight.'
	return render_template('index.html',title = title,general = general_news,entertainment = entertainment_news,technology = technology_news,business = business_news)

# Dynamic routing
@app.route('/news/<int:news_id>')
def news(news_id):
    '''
    Function that returns the news details and its data
    '''

    title = 'News Highlight'
    return render_template('news.html', id = news_id, title = title)
