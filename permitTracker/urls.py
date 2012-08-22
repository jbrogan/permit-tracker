from django.conf.urls import patterns, include, url
from views import ( 
    trainer, removeTrainer, editTrainer,
    student, removeStudent, editStudent,
    session, removeSession, editSession,
    summary, getSummary,
)

urlpatterns = patterns('',
    url(r'trainers/(\d+)/$', trainer, name='trainer_view'),
    url(r'students/(\d+)/$', student, name='student_view'),
    url(r'sessions/(\d+)/$', session, name='session_view'),
    url(r'summary/$', summary, name='summary_view'),
    url(r'summary/(\d+)/$', getSummary, name='summary_view'),
    (r'trainers/(\d+)/remove$', removeTrainer),
    (r'sessions/(\d+)/remove$', removeSession),
    (r'students/(\d+)/remove$', removeStudent),
    url(r'sessions/(\d+)/edit$', editSession, name='session_edit'),
    url(r'students/(\d+)/edit$', editStudent, name='student_edit'),
    url(r'trainers/(\d+)/edit$', editTrainer, name='trainer_edit'),
)
