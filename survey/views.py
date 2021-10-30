from django.shortcuts import render

# Create your views here.
from .models import Question,Choice
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render,get_object_or_404


def detail(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request,'survey/detail.html',{'question':question})

def index(request):
    latest_question_list = Question.objects.order_by('-q_date')[:5]
    context = {'latest_question_list':latest_question_list}
    return render(request,'survey/index.html',context)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'survey/results.html', {'question':question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'survey/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('survey:results', args=(question.id,)))