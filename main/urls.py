from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from main import views

urlpatterns = [
    path('resources', views.ResourceList.as_view()),
    # path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
