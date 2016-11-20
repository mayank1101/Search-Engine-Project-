from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Astronomy, Ai, Askubuntu
from django.contrib.postgres.search import SearchVector

def index(request):
    #if request.method == 'GET':
    return render(request,'engine/search.html')

def search_results(request):
    data_list = []
    try:
        if request.GET['val'] == 'astro':
            query = request.GET['q']
            astronomyObj = Astronomy.objects.annotate(search=SearchVector('questions')).filter(search=query)
            for obj in astronomyObj:
                data_list.append(QueryData(obj.questions[2:len(obj.questions)-2], "http://astronomy.stackexchange.com/"+obj.links[1:len(obj.links)-2],
                obj.tags[1:len(obj.tags)-1], obj.votes, obj.no_answers))
            context = {'astronomyObj': astronomyObj,'query': request.GET['q'],'data_list' : data_list,}
        elif request.GET['val'] == 'ai':
            query = request.GET['q']
            aiObj = Ai.objects.annotate(search=SearchVector('questions')).filter(search=query)
            for obj in aiObj:
                data_list.append(QueryData(obj.questions, "http://ai.stackexchange.com/"+obj.links[1:len(obj.links)-2],
                obj.tags[1:len(obj.tags)-1], obj.votes, obj.no_answers))
            context = {'aiObj': aiObj,'query': request.GET['q'],'data_list' : data_list,}
        elif request.GET['val'] == 'ubuntu':
            query = request.GET['q']
            ubuntuObj = Askubuntu.objects.annotate(search=SearchVector('questions')).filter(search=query)
            for obj in ubuntuObj:
                data_list.append(QueryData(obj.questions, "http://askubuntu.com/"+obj.links[1:len(obj.links)-2],
                obj.tags[1:len(obj.tags)-1], obj.votes, obj.no_answers))
            context = {'ubuntuObj': ubuntuObj,'query': request.GET['q'],'data_list' : data_list,}
    except Astronomy.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'engine/search_results.html', context)

class QueryData():

    def __init__(self,question,link,tags,votes,noAnswers):
        self.question = question
        self.link = link
        self.tags = tags
        self.votes = votes
        self.noAnswers = noAnswers
        if self.noAnswers is not None:
            self.noAnswers = self.noAnswers[1:len(self.noAnswers)-1]
        if self.votes is not None:
            self.votes = self.votes[1:len(self.votes)-1]
