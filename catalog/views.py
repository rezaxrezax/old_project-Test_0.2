from django.shortcuts import render_to_response, redirect
from django.template import loader
from django.template.loader import get_template
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf
from django.core.paginator import Paginator
from django.contrib import auth

from .forms import CommentForm          # add forms
from .models import Article, Comment


# Create your views here.
#----------TEST----------#
def basic_one(request):
    view = "basic_one"
    html = "<html><body>This is %s view</body></html>" % view
    return HttpResponse(html)

def basic_two(request):
    view = "basic_two"
    t = get_template('myview.html')
    html = t.render({'name': view})
    return HttpResponse(html)

def basic_three(request):
    view = "basic_three"
    return render_to_response('myview.html', {'name': view})
#----------------------------------------------------------#

def articles(request, page_number=1):
    all_articles = Article.objects.all()
    current_page = Paginator(all_articles, 2)
    return render_to_response('articles.html', {'articles': current_page.page(page_number), 'username': auth.get_user(request).username})

def article(request, article_id=1):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    args['comment'] = Comment.objects.filter(comment_article_id=article_id)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return render_to_response('article.html', args)

def addcomment(request, article_id):
    if request.POST: #and ("pause" not in request.session):                   
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment_article = Article.objects.get(id=article_id)
            form.save()
            #request.session.set_expiry(5)     #// coo
            #request.session['pause'] = True         #kie   //
    return redirect('/articles/get/%s/' % article_id)


