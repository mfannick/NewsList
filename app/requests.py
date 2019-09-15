import urllib.request,json
from .models import NewsSource,NewsArticles
# Getting api key
apiKey =None
# Getting the movie base url
webUrl =None
articleUrl=None
def config_request(app):
    global apiKey,webUrl,articleUrl
    apiKey=app.config['NEWS_API_KEY']
    webUrl=app.config['NEWS_API_WEB_URL']
    articleUrl=app.config['ARTICLES_URL']

    
    

def getNewsSource(differentNewsPub):
    '''
    Function that gets the json response to our url request
    '''
    getNewsSourceUrl=webUrl.format(differentNewsPub,apiKey)## replaces two {variables} in the webUrl from config it takes in 
     # differentNewsPub as a argument for  different news publisher
    with urllib.request.urlopen(getNewsSourceUrl) as url:#if is for requesting the url
        getNewsSourceData=url.read()# reading the response from therequest and store it
        getNewsSourceResponse= json.loads(getNewsSourceData)# convert the JSON response to a Python dictionary using json.loads function and pass in the get_movies_data 

        newsSourceResult=None
        if getNewsSourceResponse['sources']:# the sources  list that contains the news object, we use to check if the response contains any data
            newsSourceResultList=getNewsSourceResponse['sources']
            newsSourceResult=processNewsSourceResults(newsSourceResultList)
        return newsSourceResult

def processNewsSourceResults(newsSourceList):
   
    newsSourceResults=[]# this is where we will store our newly created news source objects
    for newsSourceItem in newsSourceList:#We then loop through the list of dictionaries using the get()
        url=newsSourceItem.get('url')
        id=newsSourceItem.get('id')
        name=newsSourceItem.get('name')
        description=newsSourceItem.get('description')
        category=newsSourceItem.get('category')
        language=newsSourceItem.get('language')
        

        if name:

            newsSourceObject= NewsSource(id,name,description,category,language,url)# object of values we got
            newsSourceResults.append(newsSourceObject)# apppend them in the empty list

    return newsSourceList# return the result
    '''
    Function  that processes the news Source  result and transform them to a list of Objects

    Args:
        newsSourceList: A list of dictionaries that contain news Source list details

    Returns :
        newsSourceResults: A list of news Source objects
    '''  
def getNewsArticles(id):

    getNewsArticlesUrl= articleUrl.format(id,apiKey)
    with urllib.request.urlopen(getNewsArticlesUrl) as url:
        getNewsArticlesData=url.read()
        getNewsArticlesResponse=json.loads(getNewsArticlesData)

        newsArticlesResult=None
        if getNewsArticlesUrl['articles']:
            newsArticlesResultList=getNewsArticlesResponse['articles']
            newsArticlesResult=processNewsArticlesResult(newsArticlesResultList)
        
    return newsArticlesResult

def processNewsArticlesResult(newsArticlesList):
    newsArticlesResult=[]
    for newsArticleItem in newsArticlesList:
           name=newsArticleItem.get('name')
           id=newsArticleItem.get('id')
           author=newsArticleItem.get('author')
           title=newsArticleItem.get('title')
           description=newsArticleItem.get('description')
           url=newsArticleItem.get('url')
           urlToImage=newsArticleItem.get('urlToImage')
           publishedAt=newsArticleItem.get('publishedAt')
           
           newsArticleObject= NewsArticles(id,author,title,description,url,urlToImage,publishedAt)# object of values we got
           newsArticlesResult.append(newsArticleObject)
    return newsArticlesResult




