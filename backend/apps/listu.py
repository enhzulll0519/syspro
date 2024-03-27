from apps import views
from django.urls import path
from .views import ListGetCreate, ListUpdateDelete

urlpatterns = [
    path('', ListGetCreate.as_view()),
    path('<int:pk>', ListUpdateDelete.as_view())
]