from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic

# Create your views here.
from .models import Citizen, Person


class IndexView(generic.ListView):
	template_name = 'test_app/index.html.j2'
	context_object_name = 'cit_list'

	def get_queryset(self):
		return Citizen.objects.order_by('citizen')


class DetailView(generic.DetailView):
	template_name = 'test_app/detail.html.j2'
	model = Citizen


def vote(request, citizen_id):
	citizen = get_object_or_404(Citizen, pk=citizen_id)
	try:
		selected_person = citizen.person_set.get(pk=request.POST['person'])
	except (KeyError, Person.DoesNotExist):
		return render( request,
			       'test_app/detail.html.j2',
			       {
				    'citizen': citizen,
				    'error_message': 'No person was selected',
			       },
			)
	else:
		selected_person.votes += 1
		selected_person.save()
		return HttpResponseRedirect(reverse('test:result', args=(citizen_id,)))


class ResultView(generic.DetailView):
	model = Citizen
	template_name = 'test_app/result.html.j2' 
