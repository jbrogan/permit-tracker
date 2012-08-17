from django.db import models
from account.models import MyProfile

class Trainer(models.Model):
    trainerName = models.CharField("Trainer Name", max_length=20)
    account = models.ForeignKey(MyProfile)

    def __unicode__(self):
	return str(self.trainerName)

class State(models.Model):
    state = models.CharField("State", max_length=2)

    def __unicode__(self):
	return str(self.state)

class StateRequirement(models.Model):
    state = models.ForeignKey(State)
    totalTime = models.IntegerField()
    totalNight = models.IntegerField()
    totalInclement = models.IntegerField()

    def __unicode__(self):
	return str(self.state)

class Student(models.Model):
    studentName = models.CharField("Student Name", max_length=20)
    state = models.ForeignKey(StateRequirement)
    account = models.ForeignKey(MyProfile)

    def __unicode__(self):
	return str(self.studentName)

class Session(models.Model):
    CHOICES = (('Day','Day'), ('Night','Night'))
    studentName = models.ForeignKey(Student, verbose_name="student Name")
    trainerName = models.ForeignKey(Trainer, verbose_name="trainer Name")
    account = models.ForeignKey(MyProfile)
    date = models.DateField("Date")
    driveTime = models.IntegerField("Drive Time")
    distance = models.DecimalField("Distance", max_digits=10, decimal_places=2)
    conditions = models.CharField("Conditions", choices=CHOICES, max_length=10)
    badWeather = models.BooleanField("Inclement weather")

    def __unicode__(self):
	return str(self.date)
