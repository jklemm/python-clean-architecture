from django.shortcuts import render, redirect
from django.urls.base import reverse
from django.views.generic.base import View

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
            age = int(form.cleaned_data.get('age'))

            if 18 <= age <= 60:
                Student.objects.create(
                    name=name,
                    age=age
                )
            else:
                form.add_error('age', 'The age needs to be greater or equal than 18 and lower or equal than 60!')
                return render(request, 'add.html', {'form': form})
        else:
            return render(request, 'add.html', {'form': form})

        return redirect(reverse('index'))
