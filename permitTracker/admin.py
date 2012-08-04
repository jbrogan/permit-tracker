from django.contrib import admin
from models import Trainer, StateRequirement, Student, Session, State

class StateRequirementAdmin(admin.ModelAdmin):
    fieldsets = [
	(None,		{'fields': ['state']}),
	('State Requirements', {'fields': ['totalTime', 'totalNight', 'totalInclement']}),
    ]


class SessionAdmin(admin.ModelAdmin):
    fieldsets = [
	('Driver',	{'fields': ['studentName']}),
	('Trainer',	{'fields': ['trainerName']}),
	('Date',        {'fields': ['date']}),
	('Driving',     {'fields': ['driveTime', 'distance', 'conditions']}),
    ]
    list_display = ('date', 'studentName', 'trainerName', 'driveTime', 'conditions')
    list_filter = ['date', 'studentName', 'trainerName', 'conditions']
    search_fields = ['studentName', 'trainerName']

admin.site.register(Trainer)
admin.site.register(StateRequirement, StateRequirementAdmin)
admin.site.register(Student)
admin.site.register(Session, SessionAdmin)
admin.site.register(State)
