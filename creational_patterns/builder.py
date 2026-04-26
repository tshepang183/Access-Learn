class CourseBuilder:
    def __init__(self):
        self.course = {}

    def add_title(self, title):
        self.course['title'] = title
        return self

    def add_lessons(self, lessons):
        self.course['lessons'] = lessons
        return self

    def build(self):
        return self.course