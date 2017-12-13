from core.gateways.student_gateway import StudentGateway
from students.models import Student


class StudentGatewayDjango(StudentGateway):
    def create(self, student_struct):
        Student.objects.create(
            name=student_struct.name,
            age=student_struct.age
        )

    def get_all(self):
        return Student.objects.all()
