#from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render
from django.http import HttpResponse
#from django.template import loader

from .models import Question

# Create your views here.

def TestView(View):

    def get(self, request, *args, **kwargs):
        None

    def post(self, request, rfq_id, *args, **kwargs):
        None

# path('dashboard/<str:view>', views.TestView.as_view(), name='test-view'),

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    #template = loader.get_template("polls/index.html")
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    repsonse = "You're looking at the results of question %s."
    return HttpResponse(repsonse % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on questions %s." % question_id)