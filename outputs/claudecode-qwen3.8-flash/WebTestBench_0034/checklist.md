# Test Checklist

## Functionality
- [ ] FT-01: User can register and sign in to a new account
  - Action: Open the registration page, create an account with valid credentials, then sign in with those credentials.
  - Expected: Account is created and sign-in succeeds, landing the user on the language selection/course area.

- [ ] FT-02: User can pick a language and start its course
  - Action: From the language catalog, select a language (e.g., Spanish) and choose to start the course.
  - Expected: The course dashboard for that language opens, showing its levels and lessons.

- [ ] FT-03: Course content is structured by level with lessons, exercises, and quizzes
  - Action: Open the course and inspect the curriculum layout.
  - Expected: Content is grouped into levels (e.g., Beginner → Intermediate) and each level contains lessons, exercises, and at least one quiz.

- [ ] FT-04: User can complete a lesson with exercises
  - Action: Open the first available lesson, answer its exercises, and complete the lesson.
  - Expected: Lesson is marked complete and the next lesson in the sequence becomes available.

- [ ] FT-05: User can answer multiple question types
  - Action: Within exercises/quizzes, identify and answer at least two different question formats (e.g., multiple choice and typing/translation).
  - Expected: Each question type can be answered and submitted successfully.

- [ ] FT-06: User can submit a quiz and receive a score
  - Action: Open a level's quiz, answer all questions, and click the submit/finish button.
  - Expected: A score is displayed (e.g., "7/10" or percentage) reflecting the submitted answers.

- [ ] FT-07: User can resume a course where they left off
  - Action: Complete part of a course, sign out, sign back in, and open the course.
  - Expected: A start/resume option continues from the first incomplete lesson; prior progress is preserved.

- [ ] FT-08: User can view a progress summary across lessons
  - Action: Navigate to the progress/dashboard view for the enrolled course.
  - Expected: A summary shows per-lesson status (completed vs. not) and/or quiz scores across the levels.

## Constraint
- [ ] CS-01: Cannot register with missing required fields
  - Action: Submit the registration form with required fields (e.g., email/password) left empty.
  - Expected: Registration is blocked with a visible validation error; no account is created.

- [ ] CS-02: Course content requires an authenticated account
  - Action: Without signing in, attempt to open a lesson or start a course.
  - Expected: The app does not allow starting lessons and directs the user to register/sign in.

- [ ] CS-03: Lessons follow the structured sequence (no skipping locked items)
  - Action: Attempt to open a quiz or a later lesson before completing the preceding lesson(s) in the level.
  - Expected: The locked item is visibly marked as unavailable and cannot be started until the earlier item is completed.

## Interaction
- [ ] IX-01: Instant feedback on a correct answer
  - Action: In an exercise, select/type the correct answer and click Check/Submit.
  - Expected: The answer is immediately marked correct (e.g., green highlight / "Correct" message) without a full page reload.

- [ ] IX-02: Instant feedback on a wrong answer
  - Action: In an exercise, provide an incorrect answer and click Check/Submit.
  - Expected: The answer is immediately marked wrong and the correct answer is shown.

- [ ] IX-03: Navigation between questions works
  - Action: After answering a question, click the Next button (repeat through a quiz).
  - Expected: The next question in sequence loads, and the question counter/position updates.

- [ ] IX-04: Progress indicators update immediately after completing an item
  - Action: Complete a lesson or quiz, then return to the course dashboard.
  - Expected: The lesson shows as completed and any progress bar/percentage reflects the new state without manual reset.

## Content
- [ ] CT-01: Lesson content matches the selected language
  - Action: Enroll in a specific language course (e.g., Spanish) and review several lessons.
  - Expected: All vocabulary, prompts, and answer content are in/about the chosen language — no placeholder text (e.g., Lorem Ipsum) or content from a different language.

- [ ] CT-02: Questions are complete and internally consistent
  - Action: Step through exercises and quiz questions in the course.
  - Expected: Every question has non-empty text, valid answer options, and options that match the question; no broken images or missing media.