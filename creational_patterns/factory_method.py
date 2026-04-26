class Lesson:
    def open(self):
        pass

class VideoLesson(Lesson):
    def open(self):
        return "Playing video lesson"

class TextLesson(Lesson):
    def open(self):
        return "Opening text lesson"

class LessonFactory:
    def create_lesson(self):
        pass

class VideoLessonFactory(LessonFactory):
    def create_lesson(self):
        return VideoLesson()

class TextLessonFactory(LessonFactory):
    def create_lesson(self):
        return TextLesson()