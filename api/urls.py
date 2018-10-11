from django.urls import path
from api import views

urlpatterns = [
    path('note/', views.NoteListCreateAPIView.as_view(), name='list_create'),
]
