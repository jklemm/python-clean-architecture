class StudentPresenter(object):
    def __init__(self):
        self.age_error = False

    def present_age_error_validation(self):
        self.age_error = True

    def get_errors(self):
        return [
            {
                'field': 'age',
                'message': 'The age must be >= 18 and <= 60!'
            }
        ]
