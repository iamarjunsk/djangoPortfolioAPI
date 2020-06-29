from django.urls import path
# from django.conf.urls import include
# from . import views
from .views import NotesView
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('notes',views.NotesView)

urlpatterns = [
    path('',NotesView.as_view()),
]