from creational_patterns.simple_factory import CourseFactory
from creational_patterns.singleton import Database
from creational_patterns.prototype import Lesson

def test_simple_factory():
    course = CourseFactory.create_course("math")
    assert course.name == "Mathematics"

def test_singleton():
    db1 = Database()
    db2 = Database()
    assert db1 is db2

def test_prototype():
    lesson1 = Lesson("Intro")
    lesson2 = lesson1.clone()
    assert lesson1.title == lesson2.title