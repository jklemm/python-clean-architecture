
class CreateStudentUsecase(object):

    def __init__(self, student_gateway):
        self.student_gateway = student_gateway

    def execute(self, student_struct):
        self.student_gateway.create(student_struct)
