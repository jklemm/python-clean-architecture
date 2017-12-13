from django.shortcuts import render, redirect
from django.urls.base import reverse
from django.views.generic.base import View

from core.structs.student_struct import StudentStruct
from core.usecases.create_student_usecase import CreateStudentUsecase
from gateways.student_gateway_django import StudentGatewayDjango
from students.forms import AddStudentForm
from students.models import Student


class StudentsView(View):

    def get(self, request, *args, **kwargs):
        students = Student.objects.all()
        return render(request, 'manage.html', {'students': students})


class StudentsAddView(View):

    def get(self, request, *args, **kwargs):

        form = AddStudentForm()
        return render(request, 'add.html', {'form': form})

    def post(self, request, *args, **kwargs):

        form = AddStudentForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data.get('name')
            age = form.cleaned_data.get('age')

            struct = StudentStruct(
                name=name,
                age=age
            )

            usecase = CreateStudentUsecase(
                student_gateway=StudentGatewayDjango()
            )
            usecase.execute(struct)

        else:
            return render(request, 'add.html', {'form': form})

        return redirect(reverse('index'))
