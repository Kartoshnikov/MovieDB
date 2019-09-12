from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic

# Create your views here.
from test_app.models import Citizen, Person
from .forms import UploadFileForm, TestModelForm


class IndexView(generic.ListView):
    template_name = 'test_app/index.html.j2'
    context_object_name = 'cit_list'

    def get(self, request, *args, **kwargs):
        # request.session['test'] = True
        request.session.save()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return Citizen.objects.order_by('citizen')


class DetailView(generic.DetailView):
    template_name = 'test_app/detail.html.j2'
    model = Citizen


def handle_uploaded_file(file):
    with open(r'C:\Users\Dmitriy_Kar\Downloads\web_conf.yml', 'ba') as dest:
        for chunk in file.chunks():
            dest.write(chunk)


def vote(request, citizen_id):
    citizen = get_object_or_404(Citizen, pk=citizen_id)
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            handle_uploaded_file(request.FILES['files'])
        try:
            selected_person = citizen.person_set.get(pk=request.POST['person'])
        except (KeyError, Person.DoesNotExist):
            return render(request,
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
            # return HttpResponse('Hello')


class ResultView(generic.DetailView):
    model = Citizen
    template_name = 'test_app/result.html.j2'


class UploadFormView(generic.edit.FormView):
    template_name = 'test_app/form.html.j2'
    form_class = UploadFileForm
    success_url = '/test/'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        files = request.FILES.getlist('files')
        if form.is_valid():
            for file in files:
                handle_uploaded_file(file)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class TestModelFormView(generic.edit.FormView):
    template_name = 'test_app/form.html.j2'
    form_class = TestModelForm
    success_url = '/test/'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            print(form.fields)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


# def test_session(request):
#     request.session.set_test_cookie()
#     return HttpResponse("Testing session cookie")

