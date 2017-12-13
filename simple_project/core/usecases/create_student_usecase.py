
class CreateStudentUsecase(object):

    def __init__(self, student_gateway, presenter):
        self.student_gateway = student_gateway
        self.presenter = presenter

    def execute(self, student_struct):
        if student_struct.age < 18 or student_struct.age > 60:
            self.presenter.present_age_error_validation()
            return self.presenter

        self.student_gateway.create(student_struct)
