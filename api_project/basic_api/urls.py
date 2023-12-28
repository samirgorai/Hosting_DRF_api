from django.urls import path
from basic_api import views

app_name='basic_api'

urlpatterns=[
    path('read/',views.read,name='read'),
    path('update/',views.update,name='update'),
    path('delete/',views.delete,name='delete'),
    path('create/',views.write,name='write'),
]
