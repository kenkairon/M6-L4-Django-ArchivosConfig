from django.urls import path
from . import views

app_name = 'applunes'

urlpatterns = [
    path('', views.item_list, name='item_list'),
]

"""
from django.urls import path
from applunes.views import ItemListView

urlpatterns = [
     path('', ItemListView.as_view(), name='item')
]
"""
