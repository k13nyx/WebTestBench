# Test Checklist

## Functionality
- [ ] FT-01: New user can register an account
  - Action: Open the registration page, enter valid username, email, and password, then click "Register".
  - Expected: Account is created and the user is taken to the logged-in/dashboard view.

- [ ] FT-02: User can pick a language
  - Action: From the language selection screen, select one available language (e.g., "Spanish").
  - Expected: The chosen language is saved and its course is displayed.

- [ ] FT-03: Course is organized by level
  - Action: Open the course for the selected language.
  - Expected: Lessons/exercises/quizzes appear grouped under clearly ordered levels (e.g., Beginner → Intermediate → Advanced).

- [ ] FT-04: User can start a course
  - Action: On a not-yet-started course, click "Start Course".
  - Expected: The first lesson of the first level opens and course status becomes "in progress".

- [ ] FT-05: User can resume an in-progress course
  - Action: Log out after completing part of a lesson, log back in, and click "Resume".
  - Expected: The course reopens at the last position reached, not at the beginning.

- [ ] FT-06: User can complete a lesson and its exercises
  - Action: In a lesson, answer the exercise(s) and proceed to the end, then click "Next"/"Continue".
  - Expected: The lesson is marked complete and the next lesson becomes available.

- [ ] FT-07: User can take a quiz
  - Action: Open a quiz within a level, answer all questions, and click "Submit".
  - Expected: The quiz is submitted, a score is shown, and the quiz is recorded as completed.

- [ ] FT-08: User can view a progress summary
  - Action: Open the "Progress" / "My Progress" page.
  - Expected: A summary shows which lessons are completed vs. remaining for the current course.

## Constraint
- [ ] CS-01: Registration blocked with empty required fields
  - Action: On the registration form, leave username/email/password empty and click "Register".
  - Expected: Submission is blocked and an error identifies the missing required field(s).

- [ ] CS-02: Answer cannot be submitted without a selection
  - Action: On a multiple-choice question, click "Submit" without selecting any option.
  - Expected: Submission is blocked with a prompt to choose an answer.

- [ ] CS-03: Duplicate account is rejected
  - Action: Register again using an email/username that already exists.
  - Expected: Registration fails with a "already registered / in use" message; no duplicate account is created.

- [ ] CS-04: Level sequence is enforced
  - Action: Attempt to open a later-level lesson while its prerequisite lesson/level is incomplete.
  - Expected: The locked lesson cannot be opened and shows as locked or inaccessible.

- [ ] CS-05: Course content is limited to the selected language
  - Action: After selecting one language, browse the course list.
  - Expected: Only content for the selected language is shown; no other language's lessons appear.

## Interaction
- [ ] IX-01: Instant feedback is shown after answering
  - Action: Submit an answer to a question (once correct, once incorrect).
  - Expected: Immediate feedback appears indicating correct/incorrect for that answer.

- [ ] IX-02: Score is displayed and updates
  - Action: Answer several questions/complete a quiz.
  - Expected: A simple score is shown and updates to reflect the answers given.

- [ ] IX-03: Registration shows success confirmation
  - Action: Complete registration with valid data.
  - Expected: A success confirmation/message is displayed to the user.

- [ ] IX-04: Progress indicator updates after activity
  - Action: Complete a lesson and return to the course/level view.
  - Expected: The progress indicator (bar/percentage/checkmark) reflects the newly completed lesson.

## Content
- [ ] CT-01: Lesson content matches the selected language
  - Action: Open several lessons in the chosen language's course.
  - Expected: All lesson text/vocabulary/exercises are for the selected language and its topic.

- [ ] CT-02: Levels are clearly labeled and ordered
  - Action: Inspect the course listing.
  - Expected: Each level has a readable name/label and appears in a logical progression.

- [ ] CT-03: Multiple question types are present
  - Action: Move through a lesson/quiz to its exercises.
  - Expected: More than one question format is available (e.g., multiple-choice, matching, or fill-in).

- [ ] CT-04: Progress summary accurately lists lessons
  - Action: Compare the progress page against lessons actually completed.
  - Expected: Completed and remaining lessons named in the summary match the real state of the course.