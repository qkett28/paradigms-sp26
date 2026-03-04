from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from polls.models import Question


# Create your views here.
def hello(request):
	return render(request, "polls/index.html")
