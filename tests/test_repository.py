from repositories.inmemory.inmemory_course_repository import InMemoryCourseRepository
from src.course import Course

def test_save_course():

    repo = InMemoryCourseRepository()

    course = Course("C001", "Math", "Basic Math")

    repo.save(course)

    assert repo.find_by_id("C001") == course

def test_find_all():

    repo = InMemoryCourseRepository()

    course1 = Course("C001", "Math", "Math Course")
    course2 = Course("C002", "Science", "Science Course")

    repo.save(course1)
    repo.save(course2)

    assert len(repo.find_all()) == 2

def test_delete_course():

    repo = InMemoryCourseRepository()

    course = Course("C001", "Math", "Math Course")

    repo.save(course)

    repo.delete("C001")

    assert repo.find_by_id("C001") is None