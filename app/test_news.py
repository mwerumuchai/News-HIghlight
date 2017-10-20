import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test class to test the behavior of the News class
    '''

    def setUp(self):
        '''
        Set up method that runs before each TestCase
        '''
        self.new_news = News("bbc-sport"," BBC SPORT", "Sport outline","http://www.bbc.co.uk/sport","sport")
    def test_instance(self):
        '''
        Test case that uses isinstance function
        '''
        self.assertTrue(isinstance(self.new_news,News))

    # def test_init(self):
    #     self.assertEqual(self.new_news.id,1)
    #     self.assertEqual(self.new_news.title,'Mirror')
        # self.assertEqual(self.new_news.image,'https://lh3.googleusercontent.com/MDO8iNBCRl_94UrF7Gfp1nY6Pb3V-u7JKsAwdLZNK5zo9qD2QdCvtFF9gjAMgx7KnA=w300')

if __name__ == '__main__':
    unittest.main()
