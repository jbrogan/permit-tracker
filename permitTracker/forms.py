from django.forms import ModelForm, ModelChoiceField
from permitTracker.views import Session, Trainer, Student
from permitTracker.models import State

class SessionForm(ModelForm):
    class Meta:
        model = Session
        exclude = ('account',)


class TrainerForm(ModelForm):
    class Meta:
        model = Trainer
        exclude = ('account',)


class StudentForm(ModelForm):
    state = ModelChoiceField(queryset = State.objects.order_by('state'))
    class Meta:
        model = Student
        exclude = ('account',)
        fields = ('studentName', 'state')
