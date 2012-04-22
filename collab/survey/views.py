from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the survey index.")

def detail(request, survey_id):
    return HttpResponse("You're looking at survey %s." % survey_id)

def results(request, survey_id):
    return HttpResponse("You're looking at the results of survey %s." % survey_id)

def vote(request, survey_id):
    return HttpResponse("You're voting on survey %s." % survey_id)
