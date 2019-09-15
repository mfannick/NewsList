class NewsSource:
    '''
    News source class for instantation
    '''

    def __init__(self,id,name,category,language,description,url):
      self.id=id
      self.url=url
      self.name=name
      self.category=category
      self.language=language
      self.description=description

class NewsArticles():
    '''
    News article class for instantation
    '''
    def __init__(self,name,id,author,title,description,url,urlToImage,publishedAt):
      self.name=name
      self.id=id
      self.author=author
      self.title=title
      self.description=description
      self.url=url
      self.urlToImage=urlToImage
      self.publishedAt=publishedAt