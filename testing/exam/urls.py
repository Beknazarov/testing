from django.conf.urls import url
urlpatterns = [
    url(r'^$', "exam.views.all", name='tests'),
    url(r'^show/(?P<test_id>\d+)/$', "exam.views.show", name='test'),
    url(r'^edit/(?P<test_id>\d+)/$', "exam.views.edit", name='test'),
    url(r'^new/$', "exam.views.new", name='addTest'),
]
