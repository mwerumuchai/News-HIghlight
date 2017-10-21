from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_news_source,get_articles_source

#news
@main.route('/')
def index():
	"""
	View root page function return the index page with all of its dat
	"""

	#getting news from different categories
	general_source = get_news_source('general')
	entertainment_source = get_news_source('entertainment')
	technology_source =  get_news_source('technology')
	business_source = get_news_source('business')
	title = 'Home - News Highlight.'
	return render_template('index.html',title = title,general = general_source,entertainment = entertainment_source,technology = technology_source,business = business_source)

# Dynamic routing
@main.route('/source/<id>')
def source(id):
	'''
	View Function that returns the source page and its data
	'''
	# Getting articles according to source chosen
	articles = get_articles_source(id)
	title = f'{id} - Top News'

	return render_template('source.html',title = title, article = articles)
