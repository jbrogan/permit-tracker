# Create your views here.
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from permitTracker.models import Trainer, Student, Session
from account.models import MyProfile
from django.contrib.auth.models import User
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

@login_required()
def trainer(request, userId):
    currentId = request.user.id
    #if currentId == None:
     #   return HttpResponseRedirect('/accounts/signin')
    if int(currentId) == int(userId):
        accountId = MyProfile.objects.get(user_id=currentId)
        trainer = Trainer.objects.filter(account_id=accountId.id)
        return render_to_response('trainer.html', {'trainer': trainer}, context_instance=RequestContext(request))

    else:
        return HttpResponseRedirect('/trainers/'+str(currentId))

@login_required()
def student(request, userId):
    currentId = request.user.id
    if int(currentId) == int(userId):
        accountId = MyProfile.objects.get(user_id=currentId)
        student = Student.objects.filter(account_id=accountId.id)
        return render_to_response('student.html', {'student': student}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/students/'+str(currentId))

@login_required()
def session(request, userId):
    currentId = request.user.id
    if int(currentId) == int(userId):
        accountId = MyProfile.objects.get(user_id=currentId)
        session = Session.objects.filter(account_id=accountId.id)
        return render_to_response('session.html', {'session': session}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/sessions/'+str(currentId))
