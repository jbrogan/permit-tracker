from django.conf.urls import patterns, include, url
from views import trainer, student, session, removeTrainer, removeSession, removeStudent, editSession, editTrainer

urlpatterns = patterns('',
    url(r'trainers/(\d+)/$', trainer, name='trainer_view'),
    url(r'students/(\d+)/$', student, name='student_view'),
    url(r'sessions/(\d+)/$', session, name='session_view'),
    (r'trainers/(\d+)/remove$', removeTrainer),
    (r'sessions/(\d+)/remove$', removeSession),
    (r'students/(\d+)/remove$', removeStudent),
    (r'sessions/(\d+)/edit$', editSession),
    url(r'trainers/(\d+)/edit$', editTrainer, name='trainer_edit'),
)
