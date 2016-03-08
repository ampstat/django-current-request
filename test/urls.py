from django.conf.urls import patterns, include, url

from .views import index

urlpatterns = [
    url(r'^$', index, name="index"),
]
