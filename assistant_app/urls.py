from django.urls import path
from . import views  # ← Импортируем модуль views целиком

app_name = "assistant_app"

urlpatterns = [
    path("", views.assistant_index, name="index"),
    path('contacts/', views.assistant_contacts, name='contacts'),
]