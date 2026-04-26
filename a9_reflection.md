# Reflection 

## Challenges Faced

One of the main challenges in designing the domain model and class diagram was deciding the level of abstraction. It was difficult to determine how detailed each class should be without overcomplicating the design. For example, features such as authentication and database interactions were intentionally simplified to maintain focus on the core functionality of the system.

Another challenge was identifying the correct relationships between classes. Understanding when to use simple associations versus more complex relationships such as composition required careful thought. For instance, the relationship between Course and Lesson was modeled as a one-to-many relationship because a course naturally contains multiple lessons.

Defining appropriate methods for each class was also challenging. Some methods seemed obvious, such as login() and downloadFile(), but others required thinking about actual system behavior and how users interact with the platform.

## Alignment with Previous Assignments

The class diagram aligns closely with previous assignments, including functional requirements and user stories. For example:

* The User class supports user-related actions such as accessing content.
* The Course and Lesson classes align with browsing and learning functionality from Assignment 6.
* The Download class supports offline access, which addresses the digital divide problem.
* The Settings class reflects accessibility features such as font size and low-bandwidth mode.

The state and activity diagrams from Assignment 8 also influenced the design, as they helped define how objects behave and interact within workflows.

## Trade-offs Made

Some trade-offs were made to keep the system simple and manageable. For example, inheritance was not used extensively, even though it could have been applied to roles such as Student and Lecturer. Instead, a role attribute was used within the User class to simplify the design.

Another trade-off was avoiding complex relationships such as aggregation or composition, which could make the diagram harder to understand at this stage.

## Lessons Learned

This assignment improved my understanding of object-oriented design principles. I learned how to translate system requirements into classes, attributes, and methods, and how to model relationships between objects.

I also learned that simplicity is important in early system design. A clear and well-structured model is more effective than an overly complex one.

Overall, this assignment helped bridge the gap between conceptual design and implementation, preparing the system for future development.
