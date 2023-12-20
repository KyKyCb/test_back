from django.urls import path, include

from . import views

app_name='polls'

question_urlpatterns = [
    path("", views.detail, name="avadacedavra"),
    path("results", views.results, name="results"),
    path("vote", views.vote, name="vote"),
]

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", include(question_urlpatterns)),
]
