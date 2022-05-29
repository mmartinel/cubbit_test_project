from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from data_ingestion import views

urlpatterns = [
    path('ingest/', views.EventList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
