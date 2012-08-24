# Create your views here.
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from permitTracker.models import Trainer, Student, Session, StateRequirement
from forms import SessionForm, TrainerForm, StudentForm
from account.models import MyProfile
from django.contrib.auth.models import User
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django import forms
from django.db.models import Sum

def home(request):
    return render_to_response('home.html', context_instance=RequestContext(request))

def summary(request):
    accountId = MyProfile.objects.get(user_id=request.user.id)
    student = Student.objects.filter(account_id=accountId.id)
    return render_to_response('summary.html', {'student' : student}, context_instance=RequestContext(request))

def getSummary(request, userId):
    accountId = MyProfile.objects.get(user_id=request.user.id)
    student = Student.objects.filter(account_id=accountId.id)
    stateHours = Student.objects.get(account_id=accountId.id, id=userId)
    totalHours = StateRequirement.objects.get(state_id=stateHours.state_id)
    stateTime = int(totalHours.totalTime) * 60
    time = Session.objects.filter(account_id=accountId.id, studentName_id=userId).aggregate(Sum('driveTime'))
    if time['driveTime__sum']  == None:
        percent = 0
        time['driveTime__sum'] = 0
    else:
        percent = time['driveTime__sum'] / float(stateTime)
        percent = int(round(percent,2) * 100)

    return render_to_response('summaryGet.html', {'student' : student, 'percent' : percent, 'totalTime' : totalHours.totalTime, 'completedTime' : time['driveTime__sum'] / 60}, context_instance=RequestContext(request))



@login_required()
def trainer(request, userId):
    if request.method == 'GET':
        form = TrainerForm()
        if int(request.user.id) == int(userId):
            accountId = MyProfile.objects.get(user_id=request.user.id)
            trainer = Trainer.objects.filter(account_id=accountId.id)
            return render_to_response('trainer.html', {'trainer': trainer, 'form': form}, context_instance=RequestContext(request))
        else:
            return redirect('trainer_view', request.user.id)
    elif request.method == "POST":
        accountId = MyProfile.objects.get(user_id=request.user.id)
        form = TrainerForm(request.POST)
        if form.is_valid():
            s = Trainer(account_id=accountId.id)
            f = TrainerForm(request.POST, instance=s)
            f.save()
            return redirect('trainer_view', request.user.id)
        else:
            return redirect('trainer_view', request.user.id)

@login_required()
def student(request, userId):
    if request.method == 'GET':
        form = StudentForm()
        if int(request.user.id) == int(userId):
            accountId = MyProfile.objects.get(user_id=request.user.id)
            student = Student.objects.filter(account_id=accountId.id)
            return render_to_response('student.html', {'student': student, 'form': form}, context_instance=RequestContext(request))
        else:
            return redirect('student_view', request.user.id)
    elif request.method == "POST":
        accountId = MyProfile.objects.get(user_id=request.user.id)
        form = StudentForm(request.POST)
        if form.is_valid():
            s = Student(account_id=accountId.id)
            f = StudentForm(request.POST, instance=s)
            f.save()
            return redirect('student_view', request.user.id)
        else:
            return redirect('student_view', request.user.id)

@login_required()
def session(request, userId):
    if request.method == 'GET':
        form = SessionForm()
        if int(request.user.id) == int(userId):
            accountId = MyProfile.objects.get(user_id=request.user.id)
            session = Session.objects.filter(account_id=accountId.id).order_by('-date')
            form.fields['studentName'].queryset = Student.objects.filter(account_id=accountId.id)
            form.fields['trainerName'].queryset = Trainer.objects.filter(account_id=accountId.id)
            return render_to_response('session.html', {'session': session, 'form': form}, context_instance=RequestContext(request))
        else:
            return redirect('session_view', request.user.id)
    elif request.method == "POST":
        accountId = MyProfile.objects.get(user_id=request.user.id)
        form = SessionForm(request.POST)
        if form.is_valid():
            s = Session(account_id=accountId.id)
            f = SessionForm(request.POST, instance=s)
            f.save()
            return redirect('session_view', request.user.id)
        else:
            return redirect('session_view', request.user.id)

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

@login_required()
def editStudent(request, userId):
    accountId = MyProfile.objects.get(user_id=request.user.id)
    student = Student.objects.get(account_id=accountId.id,id=userId)
    form = StudentForm(instance=student)
    return HttpResponseRedirect('#myModal')
