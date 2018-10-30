from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'polls'
router = DefaultRouter()
router.register('questions', views.QuestionViewSet)

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('api/', include(router.urls)),
]