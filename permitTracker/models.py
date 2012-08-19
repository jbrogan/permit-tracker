from django.db import models
from account.models import MyProfile

class Trainer(models.Model):
    trainerName = models.CharField("Trainer Name", max_length=20)
    account = models.ForeignKey(MyProfile)

    def __unicode__(self):
        return str(self.trainerName)

class State(models.Model):
    state = models.CharField("State", max_length=2)

    class Meta:
        ordering = ['state']

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
    state = models.ForeignKey(State)
    studentName = models.CharField("Student Name", max_length=20)
    account = models.ForeignKey(MyProfile)

    def __unicode__(self):
        return str(self.studentName)

class Session(models.Model):
    CHOICES = (('Day','Day'), ('Night','Night'))
    studentName = models.ForeignKey(Student, verbose_name="Student")
    trainerName = models.ForeignKey(Trainer, verbose_name="Trainer")
    account = models.ForeignKey(MyProfile)
    date = models.DateField("Date")
    driveTime = models.IntegerField("Driving Time")
    distance = models.IntegerField("Distance", null=True, blank=True)
    conditions = models.CharField("Conditions", choices=CHOICES, max_length=10)
    badWeather = models.BooleanField("Inclement weather")

    def __unicode__(self):
        return str(self.date)
