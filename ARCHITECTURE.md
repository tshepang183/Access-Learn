# ARCHITECTURE – AccessLearn

## 1. Project Title
AccessLearn: A Lightweight Accessible Web-Based Learning Platform

## 2. Domain
Education Technology (EdTech)

## 3. Problem Statement
Students with limited connectivity and low-end devices face exclusion from modern online learning systems. AccessLearn addresses this by providing a lightweight, accessible, and mobile-friendly learning platform.

## 4. Individual Scope
The architecture focuses on a small prototype that can be developed by one student, with room for future scaling.

## 5. C4 Model

### Level 1: System Context
**Users**
- Students
- Lecturers (future role)

**External Systems**
- Web browser
- Internet connection / mobile network
- File storage for downloadable notes

**Main System**
- AccessLearn platform

### Level 2: Container Diagram
**Frontend Web Application**
- HTML, CSS, JavaScript
- Displays pages and lessons
- Handles accessibility settings

**Local Storage**
- Saves font size and bandwidth preferences

**Static Learning Content**
- Text files for lesson notes
- Lightweight learning resources

### Level 3: Component Diagram
**Home Page Component**
- Introduces system
- Links to courses

**Course Catalogue Component**
- Displays course cards
- Supports search

**Lesson Viewer Component**
- Displays lesson content

**Accessibility Settings Component**
- Controls low-bandwidth mode
- Controls font size

**Download Notes Component**
- Provides downloadable text resources

## 6. End-to-End System Flow
1. Student opens AccessLearn in a browser.
2. Student chooses a course from the course page.
3. Student opens a lesson.
4. Student downloads text notes if needed.
5. Student enables low-bandwidth mode if internet is limited.
6. Student changes font size for better readability.

## 7. Future Architecture Extensions
- Authentication service
- Database
- Quiz engine
- Lecturer upload module
- Offline caching / PWA support

## 8. Mermaid System Context Diagram

```mermaid
flowchart TD
    Student[Student]
    Browser[Web Browser]
    AccessLearn[AccessLearn Platform]
    Notes[Downloadable Text Notes]

    Student --> Browser
    Browser --> AccessLearn
    AccessLearn --> Notes