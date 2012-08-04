from django.contrib import admin
from models import Trainer, StateRequirement, Student, Session, State

admin.site.register(Trainer)
admin.site.register(StateRequirement)
admin.site.register(Student)
admin.site.register(Session)
admin.site.register(State)
