from django.urls.conf import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns =[
    path('<int:product_id>/likes', views.like, name='like'),
]