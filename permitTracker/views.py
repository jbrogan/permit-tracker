# Django modules here
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django import forms

# Other modules here
import logging

# Our app modules here
from permitTracker.models import Trainer, Student, Session, StateRequirement
from forms import SessionForm, TrainerForm, StudentForm
from account.models import MyProfile

def home(request):
    return render_to_response('home.html', context_instance=RequestContext(request))


@login_required()
def summary(request, accountId, studentId=None):

    # If we are passed in a trainer, verify that is it a valid trainer
    if studentId is not None:
        student = get_object_or_404(Student, id=studentId)
    else:
        student = None

    # Check here to validate that this user is tied to the accountId in the URI
    # redirect to their view page if not
    account = MyProfile.objects.get(user_id=request.user.id)
    if int(accountId) != int(account.id):
        return redirect('summary_view', account.id)

    if request.method == 'GET':
        # Here we handle GET's.  If a trainer id is in the uri then we are doing
        # and edit and will display this trainer instance using the edit form, otherwise
        # display the list of trainers for this account
        if student is not None:
            student = Student.objects.filter(account_id=account.id)
            stateHours = Student.objects.get(account_id=account.id, id=studentId)
            totalHours = StateRequirement.objects.get(state_id=stateHours.state_id)
            stateTime = int(totalHours.totalTime) * 60
            time = Session.objects.filter(account_id=account.id, studentName_id=studentId).aggregate(Sum('driveTime'))
            if time['driveTime__sum']  == None:
                percent = 0
                time['driveTime__sum'] = 0
            else:
                percent = time['driveTime__sum'] / float(stateTime)
                percent = int(round(percent,2) * 100)

            return render_to_response('summaryGet.html', {'student' : student, 'percent' : percent, 'totalTime' : totalHours.totalTime, 'completedTime' : time['driveTime__sum'] / 60}, context_instance=RequestContext(request))

            
        else:
             try:
                student = Student.objects.filter(account_id=account.id)
                studentId = Student.objects.filter(account_id=account.id)[0:1].get()
             except:
                return render_to_response('summary.html', {'student' : student}, context_instance=RequestContext(request))
            
             stateHours = Student.objects.get(account_id=account.id, id=studentId.id)
             totalHours = StateRequirement.objects.get(state_id=stateHours.state_id)
             stateTime = int(totalHours.totalTime) * 60
             time = Session.objects.filter(account_id=account.id, studentName_id=studentId.id).aggregate(Sum('driveTime'))
             if time['driveTime__sum']  == None:
                 percent = 0
                 time['driveTime__sum'] = 0
             else:
                 percent = time['driveTime__sum'] / float(stateTime)
                 percent = int(round(percent,2) * 100)

             return render_to_response('summary.html', {'student' : student, 'percent' : percent, 'totalTime' : totalHours.totalTime, 'completedTime' : time['driveTime__sum'] / 60}, context_instance=RequestContext(request))
 

@login_required()
def trainer(request, accountId, trainerId=None):

    # If we are passed in a trainer, verify that is it a valid trainer
    if trainerId is not None:
        trainer = get_object_or_404(Trainer, id=trainerId)
    else:
        trainer = None

    # Check here to validate that this user is tied to the accountId in the URI
    # redirect to their view page if not
    account = MyProfile.objects.get(user_id=request.user.id)
    if int(accountId) != int(account.id):
        return redirect('trainer_view', account.id)

    if request.method == 'GET':
        # Here we handle GET's.  If a trainer id is in the uri then we are doing
        # and edit and will display this trainer instance using the edit form, otherwise
        # display the list of trainers for this account
        if trainer is not None:
            form = TrainerForm(instance=trainer)
            id = trainerId
            account_id = accountId
            return render_to_response('trainer_edit.html', locals(), context_instance=RequestContext(request))
        else:
            form = TrainerForm()
            trainer = Trainer.objects.filter(account_id=account.id)
            return render_to_response('trainer.html', locals(), context_instance=RequestContext(request))
    elif request.method == 'POST':

        # Updating existing trainer
        if trainer is not None:
            form = TrainerForm(request.POST, instance=trainer)
        else:
            # Adding new trainer
            trainer = Trainer(account_id=account.id)
            form = TrainerForm(request.POST, instance=trainer)

        if form.is_valid():
            form.save()
            return redirect('trainer_view', account.id)
        else:
            return redirect('trainer_view', account.id)

@login_required()
def student(request, accountId, studentId=None):

    # If we are passed in a trainer, verify that is it a valid trainer
    if studentId is not None:
        student = get_object_or_404(Student, id=studentId)
    else:
        student = None

    # Check here to validate that this user is tied to the accountId in the URI
    # redirect to their view page if not
    account = MyProfile.objects.get(user_id=request.user.id)
    if int(accountId) != int(account.id):
        return redirect('student_view', account.id)

    if request.method == 'GET':
        # Here we handle GET's.  If a trainer id is in the uri then we are doing
        # and edit and will display this trainer instance using the edit form, otherwise
        # display the list of trainers for this account
        if student is not None:
            form = StudentForm(instance=student)
            id = studentId
            account_id = accountId
            return render_to_response('student_edit.html', locals(), context_instance=RequestContext(request))
        else:
            form = StudentForm()
            student = Student.objects.filter(account_id=account.id)
            return render_to_response('student.html', locals(), context_instance=RequestContext(request))
    elif request.method == 'POST':

        # Updating existing trainer
        if student is not None:
            form = StudentForm(request.POST, instance=student)
        else:
            # Adding new trainer
            student = Student(account_id=account.id)
            form = StudentForm(request.POST, instance=student)
        
        if form.is_valid():
            form.save()
            return redirect('student_view', account.id)
        else:
            return redirect('student_view', account.id)


@login_required()
def session(request, accountId, studentId=None):

    # If we are passed in a trainer, verify that is it a valid trainer
    if studentId is not None:
        student = get_object_or_404(Student, id=studentId)
    else:
        student = None

    # Check here to validate that this user is tied to the accountId in the URI
    # redirect to their view page if not
    account = MyProfile.objects.get(user_id=request.user.id)
    if int(accountId) != int(account.id):
        return redirect('session_view', account.id)

    if request.method == 'GET':
        # Here we handle GET's.  If a trainer id is in the uri then we are doing
        # and edit and will display this trainer instance using the edit form, otherwise
        # display the list of trainers for this account
        if student is not None:
           studentId = int(studentId)
           form = SessionForm()
           accountId = MyProfile.objects.get(user_id=request.user.id)
           student = Student.objects.filter(account_id=accountId.id)
           try:
               studentFoo = Student.objects.get(account_id=accountId.id,id=studentId)      
           except:
               return render_to_response('sessionError.html', context_instance=RequestContext(request))
        
           session = Session.objects.filter(account_id=accountId.id,studentName=studentFoo.id).order_by('-date')
           form.fields['studentName'].queryset = Student.objects.filter(account_id=accountId.id)
           form.fields['trainerName'].queryset = Trainer.objects.filter(account_id=accountId.id)
        
           return render_to_response('session.html', {'session': session, 'form': form, 'student': student}, context_instance=RequestContext(request))
 
        else:
           form = SessionForm()
           accountId = MyProfile.objects.get(user_id=request.user.id)
           student = Student.objects.filter(account_id=accountId.id)
           session = Session.objects.filter(account_id=accountId.id).order_by('-date')
           form.fields['studentName'].queryset = Student.objects.filter(account_id=accountId.id)
           form.fields['trainerName'].queryset = Trainer.objects.filter(account_id=accountId.id)
           
           return render_to_response('session.html', {'session': session, 'form': form, 'student': student}, context_instance=RequestContext(request))

    elif request.method == 'POST':

        # Updating existing trainer
        if student is not None:
            accountId = MyProfile.objects.get(user_id=request.user.id)
            form = SessionForm(request.POST)
            if form.is_valid():
                s = Session(account_id=accountId.id)
                f = SessionForm(request.POST, instance=s)
                f.save()
                return redirect('sessionGet_view', account.id, studentId)
            else:
                return redirect('sessionGet_view', account.id, studentId)

        else:
            accountId = MyProfile.objects.get(user_id=request.user.id)
            form = SessionForm(request.POST)
            if form.is_valid():
                s = Session(account_id=accountId.id)
                f = SessionForm(request.POST, instance=s)
                f.save()
                return redirect('session_view', account.id)
            else:
                return redirect('session_view', account.id)


@login_required()
def deleteTrainer(request, accountId, trainerId):

    # Check here to validate that this user is tied to the accountId in the URI
    # redirect to their view page if not
    account = MyProfile.objects.get(user_id=request.user.id)
    if int(accountId) != int(account.id):
        return redirect('trainer_view', account.id)

    # Need to add code here that validates the following:
    # That user making the request is associated with the accountId being passed in and
    # that this account owns the trainer being passed in
    trainer = Trainer.objects.get(account_id=account.id,id=trainerId).delete()
    return redirect('trainer_view', account.id)

def deleteStudent(request, accountId, studentId):

    # Check here to validate that this user is tied to the accountId in the URI
    # redirect to their view page if not
    account = MyProfile.objects.get(user_id=request.user.id)
    if int(accountId) != int(account.id):
        return redirect('student_view', account.id)

    # Need to add code here that validates the following:
    # That user making the request is associated with the accountId being passed in and
    # that this account owns the trainer being passed in
    student = Student.objects.get(account_id=account.id,id=studentId).delete()
    return redirect('student_view', account.id)


@login_required()
def deleteSession(request, accountId, sessionId):

    # Check here to validate that this user is tied to the accountId in the URI
    # redirect to their view page if not
    account = MyProfile.objects.get(user_id=request.user.id)
    if int(accountId) != int(account.id):
        return redirect('session_view', account.id)

    # Need to add code here that validates the following:
    # That user making the request is associated with the accountId being passed in and
    # that this account owns the trainer being passed in
    session = Session.objects.get(account_id=account.id,id=sessionId).delete()
    return redirect('session_view', account.id)

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
