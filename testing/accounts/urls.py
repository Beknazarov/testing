from django.conf.urls import url
from accounts import views

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^signout/$', views.signout, name='signout'),
    url(r'^confirm/(?P<activation_key>\w+)/', views.register_confirm, name='register_confirm'),
]
