class Course:
    def __init__(self, name):
        self.name = name

class CourseFactory:
    @staticmethod
    def create_course(course_type):
        if course_type == "math":
            return Course("Mathematics")
        elif course_type == "science":
            return Course("Science")
        else:
            return Course("General")