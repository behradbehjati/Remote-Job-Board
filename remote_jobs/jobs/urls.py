from django.urls import path
from . import views
app_name='jobs'
urlpatterns=[

    path('jobs/',views.JobApiView.as_view(),name='jobview')




]