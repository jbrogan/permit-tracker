# Create your views here.
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from permitTracker.models import Trainer, Student, Session
from forms import SessionForm, TrainerForm, StudentForm
from account.models import MyProfile
from django.contrib.auth.models import User
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django import forms

@login_required()
def trainer(request, userId):
    if request.method == 'GET':
        form = TrainerForm()
        if int(request.user.id) == int(userId):
            accountId = MyProfile.objects.get(user_id=request.user.id)
            trainer = Trainer.objects.filter(account_id=accountId.id)
            return render_to_response('trainer.html', {'trainer': trainer, 'form': form}, context_instance=RequestContext(request))
        else:
            return HttpResponseRedirect('/permit/trainers/'+str(request.user.id))
    elif request.method == "POST":
        accountId = MyProfile.objects.get(user_id=request.user.id)
        form = TrainerForm(request.POST)
        if form.is_valid():
            s = Trainer(account_id=accountId.id)
            f = TrainerForm(request.POST, instance=s)
            f.save()
            return HttpResponseRedirect('/permit/trainers/'+str(request.user.id))
        else:
            return HttpResponseRedirect('/permit/trainers/'+str(request.user.id))


@login_required()
def student(request, userId):
    if request.method == 'GET':
        form = StudentForm()
        if int(request.user.id) == int(userId):
            accountId = MyProfile.objects.get(user_id=request.user.id)
            student = Student.objects.filter(account_id=accountId.id)
            return render_to_response('student.html', {'student': student, 'form': form}, context_instance=RequestContext(request))
        else:
            return HttpResponseRedirect('/permit/students/'+str(request.user.id))
    elif request.method == "POST":
        accountId = MyProfile.objects.get(user_id=request.user.id)
        form = StudentForm(request.POST)
        if form.is_valid():
            s = Student(account_id=accountId.id)
            f = StudentForm(request.POST, instance=s)
            f.save()
            return HttpResponseRedirect('/permit/students/'+str(request.user.id))
        else:
            return HttpResponseRedirect('/permit/students/'+str(request.user.id))

@login_required()
def session(request, userId):
    if request.method == 'GET':
        form = SessionForm()
        if int(request.user.id) == int(userId):
            accountId = MyProfile.objects.get(user_id=request.user.id)
            session = Session.objects.filter(account_id=accountId.id)
            return render_to_response('session.html', {'session': session, 'form': form}, context_instance=RequestContext(request))
        else:
            return HttpResponseRedirect('/permit/sessions/'+str(request.user.id))
    elif request.method == "POST":
        accountId = MyProfile.objects.get(user_id=request.user.id)
        form = SessionForm(request.POST)
        if form.is_valid():
            s = Session(account_id=accountId.id)
            f = SessionForm(request.POST, instance=s)
            f.save()
            return HttpResponseRedirect('/permit/sessions/'+str(request.user.id))
        else:
            return HttpResponseRedirect('/permit/sessions/'+str(request.user.id))


@login_required()
def removeTrainer(request, userId):
    accountId = MyProfile.objects.get(user_id=request.user.id)
    trainer = Trainer.objects.get(account_id=accountId.id,id=userId).delete()
    return redirect('trainer_view', request.user.id)

@login_required()
def removeSession(request, userId):
    accountId = MyProfile.objects.get(user_id=request.user.id)
    session = Session.objects.get(account_id=accountId.id,id=userId).delete()
    return redirect('session_view', request.user.id)

@login_required()
def removeStudent(request, userId):
    accountId = MyProfile.objects.get(user_id=request.user.id)
    student = Student.objects.get(account_id=accountId.id,id=userId).delete()
    return redirect('student_view', request.user.id)

@login_required()
def editSession(request, userId):
    accountId = MyProfile.objects.get(user_id=request.user.id)
    session = Session.objects.get(account_id=accountId.id,id=userId)
    form = SessionForm(instance=session)
    return HttpResponseRedirect('#myModal')

@login_required()
def editTrainer(request, userId):
    accountId = MyProfile.objects.get(user_id=request.user.id)
    trainer = Trainer.objects.get(account_id=accountId.id,id=userId)
    form = TrainerForm(instance=trainer)
    return HttpResponseRedirect('#myModal')
