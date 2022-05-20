from django.urls import path
from .views import BookCreate, BookDelete, BookUpdate, BookDetail, BookList

urlpatterns = [
    path('list', BookList.as_view(), name='list'),
    path('create', BookCreate.as_view(), name='create'),
    path('detail/<int:pk>', BookDetail.as_view(), name='detail'),
    path('update/<int:pk>', BookUpdate.as_view(), name='update'),
]
