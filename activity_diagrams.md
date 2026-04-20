# Activity Diagrams – AccessLearn

## Overview

These diagrams model workflows and processes within the system.

---

## 1. Browse Courses

```mermaid
flowchart TD
    A(Start) --> B(Open Website)
    B --> C(View Courses Page)
    C --> D(Select Course)
    D --> E(End)
```

### Explanation

Allows users to discover available learning content.

---

## 2. Search Courses

```mermaid
flowchart TD
    A(Start) --> B(Enter Search Term)
    B --> C(Filter Courses)
    C --> D(Display Results)
    D --> E(End)
```

### Explanation

Supports fast content discovery, improving usability.

---

## 3. View Lesson

```mermaid
flowchart TD
    A(Start) --> B(Open Course)
    B --> C(Select Lesson)
    C --> D(Display Lesson Content)
    D --> E(End)
```

### Explanation

Represents how users access learning materials.

---

## 4. Download Notes

```mermaid
flowchart TD
    A(Start) --> B(Open Lesson)
    B --> C(Click Download)
    C --> D(File Downloads)
    D --> E(End)
```

### Explanation

Supports offline learning in low-bandwidth environments.

---

## 5. Enable Low-Bandwidth Mode

```mermaid
flowchart TD
    A(Start) --> B(Open Settings)
    B --> C(Enable Low Bandwidth)
    C --> D(System Adjusts Content)
    D --> E(End)
```

### Explanation

Reduces data usage, addressing digital divide challenges.

---

## 6. Change Font Size

```mermaid
flowchart TD
    A(Start) --> B(Open Settings)
    B --> C(Change Font Size)
    C --> D(Save Preferences)
    D --> E(End)
```

### Explanation

Improves accessibility for different users.

---

## 7. Navigation Workflow

```mermaid
flowchart TD
    A(Start) --> B(Click Navigation Link)
    B --> C(Open Page)
    C --> D(End)
```

### Explanation

Ensures simple and intuitive movement between pages.

---

## 8. System Load

```mermaid
flowchart TD
    A(Start) --> B(Open Website)
    B --> C(Load Content)
    C --> D(Display Page)
    D --> E(End)
```

### Explanation

Represents system performance and responsiveness.

---

## Traceability

These workflows support:

* Functional Requirements (Assignment 4)
* User Stories (Assignment 6)
* Sprint Tasks (Assignment 6)
