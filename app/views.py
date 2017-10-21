from flask import render_template
from app import app
from .request import get_news_source,get_articles_source

#news
@app.route('/')
def index():
	"""
	new root page function return the page with all of its dat
	"""

	#getting news from different categories
	general_source = get_news_source('general')
	entertainment_source = get_news_source('entertainment')
	technology_source =  get_news_source('technology')
	business_source = get_news_source('business')
	title = 'Home - News Highlight.'
	return render_template('index.html',title = title,general = general_source,entertainment = entertainment_source,technology = technology_source,business = business_source)

# Dynamic routing
@app.route('/source/<id>')
def source(id):
	'''
	View Function that returns the source page and its data
	'''
	# Getting articles according to source chosen
	articles = get_articles_source(id)
	source_id = id.upper()
	title = f'{source_id} - Top Articles'

	return render_template('source.html',title = title,id = source_id, article = articles)
