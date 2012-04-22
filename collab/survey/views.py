from django.shortcuts import render_to_response, get_object_or_404
from survey.models import Survey, Choice
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext



def index(request):
    latest_survey_list = Survey.objects.all().order_by('-pub_date')[:5]
    return render_to_response('survey/index.html', {'latest_survey_list': latest_survey_list})

def detail(request, survey_id):
    s = get_object_or_404(Survey, pk=survey_id)
    return render_to_response('survey/detail.html', {'survey': s},
                               context_instance=RequestContext(request))


def results(request, survey_id):
    s = get_object_or_404(Survey, pk=survey_id)
    return render_to_response('survey/results.html', {'survey': s})

def vote(request, survey_id):
    s = get_object_or_404(Survey, pk=survey_id)
    try:
        selected_choice = s.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the survey voting form.
        return render_to_response('survey/detail.html', {
            'survey': s,
            'error_message': "You didn't select a choice.",
        }, context_instance=RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('survey.views.results', args=(s.id,)))
