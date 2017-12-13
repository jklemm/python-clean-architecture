from django.urls import path

from courses.views import Courses

urlpatterns = [
    path('', Courses.as_view(), name='index'),
]
