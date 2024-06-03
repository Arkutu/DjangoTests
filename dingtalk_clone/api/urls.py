from django.urls import path
from .views import  UserCreate, SendMessageView, GetMessagesView, CustomAuthToken, GroupCreate, GroupMessageCreate, GroupMessagesList, FileUploadView, GroupFilesListView



urlpatterns = [
    path('register/', UserCreate.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('send_message/', SendMessageView.as_view(), name='send_message'),
    path('get_messages/', GetMessagesView.as_view(), name='get_messages'),
    path('create_group/', GroupCreate.as_view(), name='create_group'),
    path('send_group_message/', GroupMessageCreate.as_view(), name='send_group_message'),
    path('get_group_messages/<int:group_id>/', GroupMessagesList.as_view(), name='get_group_messages'),
    path('upload_file/', FileUploadView.as_view(), name='upload_file'),
    path('get_group_files/<int:group_id>/', GroupFilesListView.as_view(), name='get_group_files'),
]   
