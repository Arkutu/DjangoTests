from django.urls import path
from .views import SendMessageView, GetMessagesView

urlpatterns = [
    path('send_message/', SendMessageView.as_view(), name='send_message'),
    path('get_messages/', GetMessagesView.as_view(), name='get_messages'),
]
