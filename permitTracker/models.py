from django.db import models

class Trainer(models.Model):
    trainerName = models.CharField(max_length=20)

    def __unicode__(self):
	return str(self.trainerName)

class State(models.Model):
    CHOICES = (('PA','PA'), ('CO','CO'))
    state = models.CharField(max_length=2, choices=CHOICES)

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
    studentName = models.CharField(max_length=20)
    state = models.ForeignKey(StateRequirement)

    def __unicode__(self):
	return str(self.studentName)

class Session(models.Model):
    CHOICES = (('Day','Day'), ('Night','Night'))
    studentName = models.ForeignKey(Student)
    trainerName = models.ForeignKey(Trainer)
    date = models.DateField()
    driveTime = models.IntegerField()
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    conditions = models.CharField(choices=CHOICES, max_length=10)

    def __unicode__(self):
	return str(self.date)
