from django.urls import path
from .views import SelfbookList

urlpatterns = [
    path('selfbooklist', SelfbookList.as_view(), name='selfbooklist'),
]
