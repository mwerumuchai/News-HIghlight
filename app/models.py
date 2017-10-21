class Source:
    '''
    News class defines news objects
    '''

    def __init__(self,id,name,description,url,category):
        '''
        __init__ method to define the properties of a Source object
        '''
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category

#articles
class Article:
	'''
	Article Class to define Article Objects
	'''
	def __init__(self,author,title,description,url,image,date):
		'''
		__init__ method to define the properties of an Article object

		'''
		self.author = author
		self.title = title
		self.description = description
		self.url = url
		self.image = image
		self.date = date
