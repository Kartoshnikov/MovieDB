from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

# Create your views here.
from test_app.models import Citizen, Person
from django.db import connection


def blocker(execute, sql, params, many, context):
    print("Execute: {}\n"
          "SQL: {}\n"
          "Params: {}\n"
          "Many: {}\n"
          "Context: {}\n".format(execute, sql, params, many, context))
    res = execute(sql, params, many, context)
    print(dir(context['connection']))
    print(dir(context['cursor']))
    # raise Exception("Access to database is blocked here")
    return res


def index(request):
    with connection.execute_wrapper(blocker):
        cit_list = Citizen.objects.order_by('citizen')
        template = loader.get_template('test_app/index.html.j2')
        return HttpResponse(template.render({'cit_list': cit_list}, request))


def detail(request, citizen_id):
    citizen = get_object_or_404(Citizen, pk=citizen_id)
    return render(request, 'test_app/detail.html.j2', {'citizen': citizen})


def vote(request, citizen_id):
    print(request.POST)
    citizen = get_object_or_404(Citizen, pk=citizen_id)
    try:
        selected_person = citizen.person_set.get(pk=request.POST['person'])
    except (KeyError) as msg:  # Person.DoesNotExist
        return render(request,
                      'test_app/detail.html.j2',
                      {
                          'citizen': citizen,
                          'error_message': msg,
                      },
                      )
    else:
        selected_person.votes += 1
        selected_person.save()
        return HttpResponseRedirect(reverse('test:result', args=(citizen_id,)))


def result(request, citizen_id):
    citizen = get_object_or_404(Citizen, pk=citizen_id)
    return render(request,
                  'test_app/result.html.j2',
                  {'citizen': citizen}
                  )
