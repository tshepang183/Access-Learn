from repositories.inmemory.inmemory_course_repository import InMemoryCourseRepository
from services.course_service import CourseService
from src.course import Course


def test_create_course():
    repo = InMemoryCourseRepository()
    service = CourseService(repo)

    course = Course("C100", "Test Course", "Description")
    service.create_course(course)

    assert repo.find_by_id("C100") == course


def test_get_course():
    repo = InMemoryCourseRepository()
    service = CourseService(repo)

    course = Course("C200", "Math", "Math Course")
    repo.save(course)

    result = service.get_course("C200")

    assert result.title == "Math"