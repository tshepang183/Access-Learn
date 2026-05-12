class CourseService:
    def __init__(self, course_repository):
        self.course_repository = course_repository

    def get_all_courses(self):
        return self.course_repository.find_all()

    def get_course(self, course_id):
        course = self.course_repository.find_by_id(course_id)
        if course is None:
            raise ValueError(f"Course {course_id} not found")
        return course

    def create_course(self, course):
        self.course_repository.save(course)
        return course

    def delete_course(self, course_id):
        self.course_repository.delete(course_id)