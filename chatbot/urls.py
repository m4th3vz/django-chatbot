from django.urls import path
from .views import ChatbotView, ChatbotAPI

urlpatterns = [
    # URL para página principal
    path('', ChatbotView.as_view(), name='chatbot'),
    path('api/chat/', ChatbotAPI.as_view(), name='chatbot_api'),
]