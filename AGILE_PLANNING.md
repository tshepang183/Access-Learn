# Agile Planning – AccessLearn

## 1. User Stories

| Story ID | User Story | Acceptance Criteria | Priority |
|---------|-----------|---------------------|----------|
| US-001 | As a student, I want to browse courses so that I can see available learning content | Courses load correctly | High |
| US-002 | As a student, I want to search courses so that I can find content quickly | Results update instantly | High |
| US-003 | As a student, I want to open lessons so that I can study content | Lesson page loads correctly | High |
| US-004 | As a student, I want to download notes so that I can study offline | File downloads successfully | High |
| US-005 | As a student, I want to enable low-bandwidth mode so that I reduce data usage | Images are removed | High |
| US-006 | As a student, I want to change font size so that I can read easily | Font updates immediately | Medium |
| US-007 | As a user, I want simple navigation so that I can move easily between pages | Links work correctly | High |
| US-008 | As a lecturer, I want to upload content so that students can access it | Upload feature works | Low |
| US-009 | As an admin, I want system stability so that users have a smooth experience | System loads consistently | Medium |
| US-010 | As a system, I want fast loading pages so that users save data | Loads within 2 seconds | High |

---

## 2. Product Backlog

| Story ID | User Story | Priority (MoSCoW) | Effort (Points) | Dependencies |
|---------|-----------|------------------|----------------|--------------|
| US-001 | Browse courses | Must-have | 3 | None |
| US-002 | Search courses | Must-have | 3 | US-001 |
| US-003 | Open lesson | Must-have | 2 | US-001 |
| US-004 | Download notes | Must-have | 2 | US-003 |
| US-005 | Low-bandwidth mode | Must-have | 3 | None |
| US-006 | Change font size | Should-have | 2 | None |
| US-007 | Navigation | Must-have | 2 | None |
| US-008 | Upload content | Could-have | 5 | Backend needed |
| US-009 | System stability | Should-have | 3 | All features |
| US-010 | Fast performance | Must-have | 3 | Optimization |

### Justification

Must-have features are critical for system usability and directly address the digital divide problem.  
Should-have features improve user experience.  
Could-have features are future improvements.

---

## 3. Sprint Planning

### Sprint Goal
Deliver a functional MVP that allows students to browse courses, view lessons, and download notes in a low-bandwidth environment.

---

### Selected User Stories (Sprint 1)

- US-001 Browse courses  
- US-002 Search courses  
- US-003 Open lesson  
- US-004 Download notes  
- US-005 Low-bandwidth mode  

---

### Sprint Backlog

| Task ID | Task Description | Assigned To | Hours | Status |
|--------|----------------|------------|-------|--------|
| T-001 | Create courses page UI | Developer | 5 | To Do |
| T-002 | Implement search function | Developer | 6 | To Do |
| T-003 | Build lesson page | Developer | 5 | To Do |
| T-004 | Add download notes feature | Developer | 4 | To Do |
| T-005 | Implement low-bandwidth mode | Developer | 5 | To Do |

---

### How this supports MVP

This sprint delivers the core learning functionality, ensuring students can access content even with limited internet.

---

## 4. Reflection

One of the main challenges in this assignment was prioritizing features while balancing user needs and technical feasibility. As the only stakeholder, it was difficult to decide what should be included in the MVP versus what could be postponed.

There was also internal resistance when estimating effort, as some features seemed simple but required deeper analysis when broken into tasks.

Another challenge was aligning user stories with previous requirements and use cases to ensure consistency across assignments.

Overall, this assignment helped in understanding Agile principles such as prioritization, sprint planning, and iterative development.