from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Question, Choice


# Create your views here.

@login_required()
def index(request):
    """Function that executes with path: '/'
    
    :param request: The http request Object that is parsed.
    :type request: HttpRequest
     
    :return: The rendered template "poll.html" with the context containing the latest question list.
    :rtype: HttpResponse
"""
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/poll.html", context)

@login_required()
def detail(request, question_id):
    """Function that executes with path: '<int:question_id>'
    
    :param request: The http request Object that is parsed.
    :type request: HttpRequest

    :param question_id: The ID of the question.
    :type question_id: int
    
    :raises Http404: If the question with the given ID does not exist.
     
    :return: The rendered template "polls/detail.html" with the context containing the latest question list.
    :rtype: HttpResponse
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

@login_required()
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

@login_required()
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
       
        return render(
            request,
            "polls/detail.html",
            {"question": question, "error_message": "You didn't select a choice."},
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
    
        return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))

