from fastapi import FastAPI, HTTPException
from src.course import Course
from repositories.inmemory.inmemory_course_repository import InMemoryCourseRepository
from services.course_service import CourseService

app = FastAPI(
    title="AccessLearn API",
    description="REST API for managing courses",
    version="1.0.0"
)

repository = InMemoryCourseRepository()
service = CourseService(repository)

# Seed sample data
repository.save(Course("C001", "Mathematics", "Basic Mathematics"))
repository.save(Course("C002", "Science", "Introduction to Science"))


@app.get("/api/courses")
def get_all_courses():
    return [
        {
            "course_id": c.course_id,
            "title": c.title,
            "description": c.description
        }
        for c in service.get_all_courses()
    ]


@app.get("/api/courses/{course_id}")
def get_course(course_id: str):
    try:
        c = service.get_course(course_id)
        return {
            "course_id": c.course_id,
            "title": c.title,
            "description": c.description
        }
    except ValueError:
        raise HTTPException(status_code=404, detail="Course not found")


@app.post("/api/courses")
def create_course(course: dict):
    new_course = Course(
        course["course_id"],
        course["title"],
        course["description"]
    )
    service.create_course(new_course)
    return {"message": "Course created successfully"}


@app.delete("/api/courses/{course_id}")
def delete_course(course_id: str):
    service.delete_course(course_id)
    return {"message": "Course deleted successfully"}