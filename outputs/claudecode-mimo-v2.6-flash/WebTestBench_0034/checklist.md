# Test Checklist

## Functionality
- [ ] FT-01: Register a new account
  - Action: Navigate to the registration form, enter a valid email and password, and submit.
  - Expected: Account is created and the user is signed in, landing on a language selection or dashboard page.

- [ ] FT-02: Choose a language to learn
  - Action: On the language selection screen, pick one of the offered languages and confirm.
  - Expected: The selected language becomes the user's active course and the course page for that language opens.

- [ ] FT-03: Course displays lessons grouped by level
  - Action: Open the selected language's course page.
  - Expected: Lessons are listed under distinct levels (e.g., Beginner, Intermediate) in a clear sequence.

- [ ] FT-04: Start a course from the beginning
  - Action: Click the start/begin button on a course with no prior progress.
  - Expected: The first lesson opens, showing lesson content followed by exercises.

- [ ] FT-05: Resume an in-progress course
  - Action: Leave a lesson mid-way, return to the course page, and click resume/continue.
  - Expected: The app reopens the lesson/step the user left off on, not the beginning.

- [ ] FT-06: Complete a lesson and advance to the next
  - Action: Finish all exercises in a lesson and submit/continue.
  - Expected: The lesson is marked complete and the next lesson in the sequence becomes accessible.

- [ ] FT-07: Answer a multiple-choice question
  - Action: In an exercise, select an option and submit the answer.
  - Expected: The answer is accepted, recorded, and the exercise advances or accepts completion.

- [ ] FT-08: Answer a typed/text-input question
  - Action: Type an answer into a free-text exercise field and submit.
  - Expected: The response is accepted and evaluated rather than rejected as invalid input.

- [ ] FT-09: Answer a matching or ordering-style question
  - Action: Complete an exercise requiring matching pairs or arranging items, then submit.
  - Expected: The arrangement/matching is accepted and evaluated.

- [ ] FT-10: Take a quiz at the end of a lesson or level
  - Action: Navigate to a quiz and answer all questions, then submit.
  - Expected: The quiz submits successfully and produces a score result.

- [ ] FT-11: View a progress summary
  - Action: Open the progress/summary view.
  - Expected: A summary shows completed vs. remaining lessons for the chosen language and overall progress.

## Constraint
- [ ] CS-01: Registration blocked with invalid or empty credentials
  - Action: Submit the registration form with an empty email/password or malformed email.
  - Expected: Submission is blocked and a validation error is displayed; no account is created.

- [ ] CS-02: Cannot skip ahead to locked lessons
  - Action: Attempt to open a lesson that comes after an incomplete prior lesson.
  - Expected: Access is prevented (locked state or error) until prerequisite lessons are completed.

- [ ] CS-03: Cannot submit an exercise or quiz question with no answer selected/entered
  - Action: Leave a question unanswered and click submit/next.
  - Expected: The app blocks advancement and prompts the user to answer.

- [ ] CS-04: Duplicate registration with an existing email is rejected
  - Action: Register using an email already registered.
  - Expected: Registration fails with an "already exists" style error message.

## Interaction
- [ ] IX-01: Instant feedback shown after each answer
  - Action: Submit an answer to any exercise or quiz question.
  - Expected: Immediate visual feedback appears indicating correct or incorrect, before moving on.

- [ ] IX-02: Score updates after answering questions
  - Action: Answer questions in a quiz/exercise set.
  - Expected: A visible score/points indicator reflects the results of answered questions.

- [ ] IX-03: Course state reflects progress after leaving and returning
  - Action: Complete part of a course, refresh or revisit the course page.
  - Expected: The UI shows updated progress (e.g., completed lessons marked, continue option present) without loss of state.

## Content
- [ ] CT-01: Lesson content matches the selected language and level
  - Action: Open lessons at different levels of the chosen language.
  - Expected: All lesson text, vocabulary, and questions are in/about the selected language and appropriate to the stated level.

- [ ] CT-02: Answer options and quiz content are relevant and non-duplicated
  - Action: Review multiple-choice options and quiz questions across exercises.
  - Expected: Options are plausible, distinct, and on-topic; no lorem-ipsum or off-theme placeholder content appears.

- [ ] CT-03: Progress summary values are accurate
  - Action: Compare the progress summary against actual completed lessons.
  - Expected: Counts of completed/remaining lessons and score shown match what the user actually finished.