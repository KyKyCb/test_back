from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import (
    HttpResponse,
    render,
    get_list_or_404,
    get_object_or_404,
    HttpResponseRedirect,
)
from django.http import HttpRequest, HttpResponseNotFound
from django.urls import reverse
from django.views import generic
from .models import Question, Choice
from django.utils import timezone

def questionMapper(question: Question):
    questiondict = {
        "id": question.pk,
        "pub_date": question.pub_date.isoformat(timespec="seconds"),
        "question": question.question_text,
    }
    return questiondict

class IndexView(generic.ListView):
    template_name='polls/index.html'
    context_object_name='latest_question_list'

    def get_queryset(self) -> QuerySet[Question]:

        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:10]
class DetailView(generic.DetailView):
    template_name='polls/details.html'
    model=Question

    def get_queryset(self) -> QuerySet[Question]:
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    template_name='polls/results.html'
    model=Question

def vote(request: HttpRequest, question_id: int):
    method = request.method
    post_body = request.POST

    if method.lower() != "post":
        return HttpResponseNotFound()
    question = get_object_or_404(Question, pk=question_id)
    try:
        choice = Choice.objects.get(pk=post_body["choice"], question=question)
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/details.html",
            {
                "question": question,
                "error_message": "Choice id is not defined or invalid",
            },
        )
    else:
        choice.votes += 1
        choice.save()

        return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))
