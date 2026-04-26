class Course:
    def __init__(self, course_id, title, description):
        self.course_id = course_id
        self.title = title
        self.description = description

    def view_course(self):
        return self.title