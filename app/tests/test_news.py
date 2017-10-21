import unittest
from app.models import News
News = news.News

class NewsTest(unittest.TestCase):
	"""
	Test case to test the behaviour of the news class
	"""

	def setUp(self):
		"""
		set up method that will run before every test
		"""
		self.new_news_source = News("abc-news-au","ABC News (AU)","Australia's most trusted source of local, national and world news. Comprehensive, independent, in-depth analysis, the latest business, sport, weather and more.","http://www.abc.net.au/news","general")

	def test_instance(self):
		self.assertTrue(isinstance(self.new_news_source,News))

	def test_init(self):
		"""
		test_init test case to test if the object is initialized porperly
		"""

		self.assertEqual(self.new_news_source.id,"abc-news-au")
		self.assertEqual(self.new_news_source.name,"ABC News (AU)")
		self.assertEqual(self.new_news_source.description,"Australia's most trusted source of local, national and world news. Comprehensive, independent, in-depth analysis, the latest business, sport, weather and more.")
		self.assertEqual(self.new_news_source.url,"http://www.abc.net.au/news")

# if __name__ == '__main__':
#   unittest.main()
