from django.urls import path, include

from . import views

app_name='polls'

question_urlpatterns = [
    path("", views.DetailView.as_view(), name="avadacedavra"),
    path("results", views.ResultsView.as_view(), name="results"),
]

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", include(question_urlpatterns)),
    
    path("<int:question_id>/vote", views.vote, name="vote"),
]
