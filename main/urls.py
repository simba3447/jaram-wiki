from django.conf.urls import url
from main.views import *

urlpatterns = [
    url('^', MainView.as_view(), name = 'homepage_main'),
]
