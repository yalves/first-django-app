from django.urls import path

from . import apiviews
from . import views

app_name = 'polls'
urlpatterns = [
    # /polls/
    path('', views.IndexView.as_view(), name='index'),
    # /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('questions/', apiviews.questions_view, name='questions_view'),
    path('questions/<int:question_id>/', apiviews.question_detail_view, name='question_detail_view'),
]