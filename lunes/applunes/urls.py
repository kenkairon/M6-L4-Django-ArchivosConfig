from django.urls import path
from applunes.views import ItemListView

urlpatterns = [
     path('', ItemListView.as_view(), name='item')
]