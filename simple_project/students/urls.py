from django.urls import path

from students.views import StudentsView, StudentsAddView

urlpatterns = [
    path('manage', StudentsView.as_view(), name='index'),
    path('add', StudentsAddView.as_view(), name='students_add')
]
