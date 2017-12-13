from django.shortcuts import render, redirect
from django.urls.base import reverse
from django.views.generic.base import View

from core.structs.student_struct import StudentStruct
from core.usecases.create_student_usecase import CreateStudentUsecase
from gateways.student_gateway_django import StudentGatewayDjango
from presenters.student_presenter import StudentPresenter
from students.forms import AddStudentForm


class StudentsView(View):

    def get(self, request, *args, **kwargs):
        student_gateway = StudentGatewayDjango()
        students = student_gateway.get_all()
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

            presenter = StudentPresenter()

            usecase = CreateStudentUsecase(
                student_gateway=StudentGatewayDjango(),
                presenter=presenter
            )
            presenter = usecase.execute(struct)
            
            if presenter:
                for error in presenter.get_errors():
                    form.add_error(error['field'], error['message'])
                return render(request, 'add.html', {'form': form})

        else:
            return render(request, 'add.html', {'form': form})

        return redirect(reverse('index'))
