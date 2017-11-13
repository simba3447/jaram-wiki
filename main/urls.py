from django.conf.urls import url
import django.contrib.auth.views
from .views import MainView, ProfileView


urlpatterns = [
    url(r'^$', MainView.as_view(), name='homepage_main'),
    url(r'^profile/', ProfileView.as_view(), name='profile'),
    url(r'^login/', django.contrib.auth.views.login,
        name='login', kwargs={'template_name': 'main/login.html'}),
    # url(r'^logout', django.contrib.auth.views.logout, name='logout', kwargs={'next_page': '/'}),
    # url(r'^sign_up', SignUpView.as_view(), name='sign_up'),
]
