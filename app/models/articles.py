
#articles
class Article:
	'''
	Article Class to define Article Objects
	'''
	def __init__(self,author,title,description,url,image,date):
		'''
		Function to initialize Article Objects. Defines the properties each Article object will hold.

		Args:

		'''
		self.author = author
		self.title = title
		self.description = description
		self.url = url
		self.image = image
		self.date = date
