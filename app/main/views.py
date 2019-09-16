
from flask import render_template,request,redirect,url_for
from . import main
from ..requests import getNewsSource,getNewsArticles



@main.route('/')
def newsSource():
    '''
    View root page function that returns the newsSource page and its data
    '''
    title='News List app'
    general=getNewsSource('general')
    business=getNewsSource('business')
    technology=getNewsSource('technology')
    
    return render_template('newsSource.html',title=title,general=general,business=business,technology=technology)


@main.route('/articles/<id>')
def newsArticles(id):
    '''
    View movie page function that returns the movie details page and its data
    '''
    title='News List app'
    articles=getNewsArticles(id)
    return render_template('newsArticles.html',title=title,articles=articles)