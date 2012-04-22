from django.shortcuts import render_to_response
from survey.models import Survey
from django.http import HttpResponse

def index(request):
    latest_survey_list = Survey.objects.all().order_by('-pub_date')[:5]
    return render_to_response('survey/index.html', {'latest_survey_list': latest_survey_list})

def detail(request, survey_id):
    return HttpResponse("You're looking at survey %s." % survey_id)

def results(request, survey_id):
    return HttpResponse("You're looking at the results of survey %s." % survey_id)

def vote(request, survey_id):
    return HttpResponse("You're voting on survey %s." % survey_id)
