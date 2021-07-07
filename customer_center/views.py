from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Question

# Create your views here.
class QuestionList(ListView):
    model = Question
    ordering='-pk'
    template_name = 'customer_center/question_list.html'

class QuestionDetail(DetailView):
    model=Question













