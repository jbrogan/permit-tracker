from django.forms import ModelForm, ModelChoiceField
from permitTracker.views import Session, Trainer, Student
from permitTracker.models import StateRequirement

class SessionForm(ModelForm):
    class Meta:
        model = Session
        exclude = ('account',)


class TrainerForm(ModelForm):
    class Meta:
        model = Trainer
        exclude = ('account',)


class StudentForm(ModelForm):
    state = ModelChoiceField(queryset = StateRequirement.objects.order_by('state'))
    class Meta:
        model = Student
        exclude = ('account',)
