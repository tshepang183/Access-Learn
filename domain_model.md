# Domain Model – AccessLearn

## Overview

The domain model represents the core entities (objects) of the AccessLearn system, including their attributes, methods, and relationships.

---

## Classes and Descriptions

### 1. User

| Attribute | Description         |
| --------- | ------------------- |
| userId    | Unique identifier   |
| name      | User name           |
| role      | Student or Lecturer |

**Methods**

* login()
* logout()

---

### 2. Course

| Attribute   | Description    |
| ----------- | -------------- |
| courseId    | Unique ID      |
| title       | Course name    |
| description | Course details |

**Methods**

* viewCourse()

---

### 3. Lesson

| Attribute | Description    |
| --------- | -------------- |
| lessonId  | Unique ID      |
| title     | Lesson title   |
| content   | Lesson content |

**Methods**

* openLesson()

---

### 4. Download

| Attribute | Description     |
| --------- | --------------- |
| fileId    | File identifier |
| fileName  | Name of file    |
| fileSize  | Size of file    |

**Methods**

* downloadFile()

---

### 5. Settings

| Attribute     | Description     |
| ------------- | --------------- |
| fontSize      | User preference |
| bandwidthMode | Low/Normal      |

**Methods**

* changeFontSize()
* enableLowBandwidth()

---

### 6. Search

| Attribute | Description    |
| --------- | -------------- |
| query     | Search keyword |

**Methods**

* searchCourse()

---

### 7. Session

| Attribute | Description     |
| --------- | --------------- |
| sessionId | Unique ID       |
| status    | Active/Inactive |

**Methods**

* startSession()
* endSession()

---

## Relationships

| Relationship      | Description                     |
| ----------------- | ------------------------------- |
| User → Course     | A user can view many courses    |
| Course → Lesson   | A course contains many lessons  |
| Lesson → Download | A lesson has downloadable notes |
| User → Settings   | Each user has settings          |
| User → Session    | A user has one active session   |
| User → Search     | A user performs searches        |

---

## Business Rules

* A user must select a course before accessing lessons
* A lesson must be opened before downloading notes
* Settings are saved per user
* Low-bandwidth mode removes heavy content
