from django.urls import path
from test_app import views

app_name = 'test'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # path('session/', views.test_session),
    path('formU/', views.UploadFormView.as_view(), name='form'),
    path('formT/', views.TestModelFormView.as_view(), name='form'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/result/', views.ResultView.as_view(), name='result'),
    path('<int:citizen_id>/vote/', views.vote, name='vote'),
]
