from django.urls import path

from . import views


app_name = 'conversations'


urlpatterns = [
    path('new/<int:item_pk>/', views.new_conversation, name='newcon'),
    path('', views.inbox, name='inbox'),
    path('<int:pk>/', views.detail, name='detail')
]
