from flask import render_template
from app import app
from .request import get_news_source

#views
@app.route('/')
def index():
    '''
    Function that returns the index page and its data
    '''

    # getting top news highlights
    latest_news = get_news_source("category")
    print(latest_news)
    title = 'Home - News Highlight'
    return render_template('index.html', title = title, category = latest_news)

# Dynamic routing
@app.route('/news/<int:news_id>')
def news(news_id):
    '''
    Function that returns the news details and its data
    '''

    title = 'News Highlight'
    return render_template('news.html', id = news_id, title = title)
