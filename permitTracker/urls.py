from django.conf.urls import patterns, include, url
from views import ( 
    trainer, deleteTrainer, editTrainer,
    student, removeStudent, editStudent,
    session, removeSession, editSession,
    summary, getSummary, getSession,
)

urlpatterns = patterns('',
    url(r'(\d+)/trainers/$', trainer, name='trainer_view'),
    url(r'(\d+)/trainers/(\d+)/$', trainer, name='trainer_view'),
    url(r'(\d+)/trainers/(\d+)/edit$', trainer, name='trainer_edit'),
    url(r'(\d+)/trainers/(\d+)/delete$', deleteTrainer, name='trainer_delete'),
    url(r'students/(\d+)/$', student, name='student_view'),
    (r'students/(\d+)/remove$', removeStudent),
    url(r'students/(\d+)/edit$', editStudent, name='student_edit'),
    url(r'sessions/$', session, name='session_view'),
    url(r'sessions/(\d+)/$', getSession, name='session_view'),
    (r'sessions/(\d+)/remove$', removeSession),
    url(r'sessions/(\d+)/edit$', editSession, name='session_edit'),
    url(r'summary/$', summary, name='summary_view'),
    url(r'summary/(\d+)/$', getSummary, name='summary_view'),
)
