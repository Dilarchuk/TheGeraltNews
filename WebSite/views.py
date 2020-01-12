from django.views import View
from django.shortcuts import render
from WebSite.models import *


# Create your views here.
class Home(View):
    data = {}  # словарь куда мы все заносим

    def get(self, request):
        self.data['articles'] = Article.objects.all()

        return render(request, 'index.html', self.data)
class ArticleView(View):
    def get(self, request, post_id):
        article = Article.objects.filter(id=post_id).values ()[0] #за каждой строчкой закреплен йади, будет браться сточка только с этим йади.
        return render(request, 'news.html', article)
