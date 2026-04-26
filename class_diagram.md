# Class Diagram – AccessLearn

## Mermaid Class Diagram

```mermaid
classDiagram

class User {
-userId: String
-name: String
-role: String
+login()
+logout()
}

class Course {
-courseId: String
-title: String
-description: String
+viewCourse()
}

class Lesson {
-lessonId: String
-title: String
-content: String
+openLesson()
}

class Download {
-fileId: String
-fileName: String
-fileSize: Number
+downloadFile()
}

class Settings {
-fontSize: String
-bandwidthMode: String
+changeFontSize()
+enableLowBandwidth()
}

class Search {
-query: String
+searchCourse()
}

class Session {
-sessionId: String
-status: String
+startSession()
+endSession()
}

User "1" -- "0..*" Course : views
Course "1" -- "1..*" Lesson : contains
Lesson "1" -- "0..1" Download : has
User "1" -- "1" Settings : owns
User "1" -- "1" Session : has
User "1" -- "0..*" Search : performs
```

---

## Explanation of Design

* The **User class** is the central entity interacting with all other components.
* A **Course contains multiple Lessons**, reflecting structured learning.
* A **Lesson may have a Download**, supporting offline learning.
* **Settings are linked to a single user**, ensuring personalization.
* **Session tracks user activity**, aligning with system interaction tracking.
* **Search enables course discovery**, improving usability.

The design focuses on simplicity and scalability, making it suitable for a lightweight system.
