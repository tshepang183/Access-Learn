class Lesson:
    def __init__(self, lesson_id, title, content):
        self.lesson_id = lesson_id
        self.title = title
        self.content = content

    def open_lesson(self):
        return self.content