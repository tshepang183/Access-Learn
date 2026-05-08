from repositories.course_repository import CourseRepository

class InMemoryCourseRepository(CourseRepository):

    def __init__(self):
        self._storage = {}

    def save(self, course):
        self._storage[course.course_id] = course

    def find_by_id(self, course_id):
        return self._storage.get(course_id)

    def find_all(self):
        return list(self._storage.values())

    def delete(self, course_id):
        if course_id in self._storage:
            del self._storage[course_id]