from django.conf.urls import patterns, include, url
from views import trainer, student, session, removeTrainer, removeSession, removeStudent, editSession

urlpatterns = patterns('',
    (r'trainers/(\d+)/$', trainer),
    (r'students/(\d+)/$', student),
    (r'sessions/(\d+)/$', session),
    (r'trainers/(\d+)/remove$', removeTrainer),
    (r'sessions/(\d+)/remove$', removeSession),
    (r'students/(\d+)/remove$', removeStudent),
    (r'sessions/(\d+)/edit$', editSession),
)
