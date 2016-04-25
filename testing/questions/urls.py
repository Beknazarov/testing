from django.conf.urls import url
urlpatterns = [
    url(r'^show/(?P<question_id>\d+)/$', "questions.views.show", name='question'),
    url(r'^edit/(?P<question_id>\d+)/$', "questions.views.edit", name='edit'),
    url(r'^new/(?P<test_id>\d+)/$', "questions.views.new", name='new_question'),
]
