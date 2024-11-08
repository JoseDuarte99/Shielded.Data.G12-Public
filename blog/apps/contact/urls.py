from django.urls import path
from . import views

app_name = 'apps.contact'

urlpatterns = [
    path("", views.ContactUsuer.as_view(), name='contact'),
    path("success", views.ContactSuccess.as_view(), name='contact_success'),
    path("messages", views.MessagesListView.as_view(), name='messages'),
    path("messages-detail/<int:id>/", views.MessagesDetailView.as_view(), name='message_detail'),
    path("message_delete/<int:id>/", views.MessagesDeleteView.as_view(), name='message_delete'),
]