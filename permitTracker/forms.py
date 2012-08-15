from django.forms import ModelForm
from permitTracker.views import Session, Trainer, Student

class SessionForm(ModelForm):
    class Meta:
        model = Session
        exclude = ('account',)


class TrainerForm(ModelForm):
    class Meta:
        model = Trainer
        exclude = ('account',)


class StudentForm(ModelForm):
    class Meta:
        model = Student
        exclude = ('account',)
