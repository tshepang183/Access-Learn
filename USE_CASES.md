# Use Case Modeling – AccessLearn

## 1. Use Case Diagram

```mermaid
flowchart TD

Student --> BrowseCourses
Student --> SearchCourses
Student --> ViewLesson
Student --> DownloadNotes
Student --> AdjustSettings

Lecturer --> UploadContent
Admin --> ManageSystem
IT --> MaintainSystem
Government --> MonitorAccess

BrowseCourses --> ViewLesson
SearchCourses --> ViewLesson
ViewLesson --> DownloadNotes