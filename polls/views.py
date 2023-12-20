from django.shortcuts import HttpResponse, render, get_list_or_404, get_object_or_404
from django.http import HttpRequest
from .models import Question


def questionMapper(question: Question):
    questiondict = {
        "id": question.pk,
        "pub_date": question.pub_date.isoformat(timespec="seconds"),
        "question": question.question_text,
    }
    return questiondict


# Create your views here.
def index(request: HttpRequest):
    allQuestions = get_list_or_404(Question.objects.order_by("pub_date")[:10])
    context = {"latest_question_list": allQuestions}

    return render(request, "polls/index.html", context)


def detail(request: HttpRequest, question_id: int):
    question_item = get_object_or_404(Question, pk=question_id)
    context = {"details": question_item}

    return render(request, "polls/details.html", context)


def results(request: HttpRequest, question_id: int):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request: HttpRequest, question_id: int):
    return HttpResponse("You're voting on question %s." % question_id)
