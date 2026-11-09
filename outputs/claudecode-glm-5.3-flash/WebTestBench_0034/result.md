All checks complete. Here is the full test report:

# Test Result

## Functionality
- [X] FT-01: New user can register an account
  - Action: Fill in the registration form (e.g., name, email, password) and click the "Sign Up" / "Register" button.
  - Expected: Registration succeeds and the user is logged in / taken to the main dashboard.

- [ ] FT-02: Registered user can log in with valid credentials
  - Action: Enter the credentials used in FT-01 and click "Log In".
  - Expected: User reaches their dashboard showing their available courses/progress.
  - Bug Report:
    - Issue: Login always rejects valid credentials ("Invalid email or password")
    - Actual: Logging in with exactly `testuser01@example.com` / `Passw0rd123` (verified input order: email field, password field) returns "Invalid email or password" and stays on /login. Retried multiple times; a second freshly-registered account (`testuser02@example.com` / `TestPass99`) also fails to log in after logout. Once logged out, the user can never log back in, even though the account exists (duplicate registration is correctly rejected).

- [X] FT-03: User can pick a language from the language selection
  - Action: Open the language selection (e.g., a list of languages on the dashboard) and select one language (e.g., "Spanish").
  - Expected: The chosen language's course/level structure is displayed.

- [ ] FT-04: Course content is organized by level with lessons, exercises, and quizzes
  - Action: View the selected language's course overview.
  - Expected: Multiple levels are shown, each containing a sequence of lessons, exercises, and quizzes in order.
  - Bug Report:
    - Issue: Missing content type — no quizzes in the course structure
    - Actual: Levels are shown (Beginner with 3 items, Elementary with 2 items) and lessons appear in order, but every course item is a lesson ("4 questions"); there are no standalone exercise items and no quiz items anywhere in either level. Exercises (multiple choice, translation, fill-in-the-blank) are embedded inside lessons, but no quiz exists to complete the level sequence.

- [X] FT-05: User can start a lesson and view its content
  - Action: Click the first available lesson in the sequence.
  - Expected: The lesson opens and displays its learning content (vocabulary, phrases, or grammar material).

- [X] FT-06: User can complete an exercise with multiple-choice questions
  - Action: Answer a multiple-choice exercise by selecting an option and submitting.
  - Expected: The answer is accepted and recorded.

- [X] FT-07: User can answer typed/fill-in-the-blank questions
  - Action: Type an answer into a text input for a translation or fill-in-the-blank exercise and submit.
  - Expected: The typed answer is accepted and evaluated.

- [ ] FT-08: User can complete a quiz at the end of a level
  - Action: Answer all questions in a quiz and submit it.
  - Expected: The quiz finishes and a score/result is shown.
  - Bug Report:
    - Issue: Feature missing — no quiz exists at the end of a level
    - Actual: Completed all Level 1 lessons (Greetings, Numbers 1-10, Colors) and Level 1 reached 3/3, but no quiz item appeared or unlocked; the course contains only lessons, each ending in a "Lesson Complete!" score screen. A dedicated level-end quiz does not exist, so this item cannot be performed.

- [ ] FT-09: User can resume a course at the last unfinished item
  - Action: Complete part of a course, log out, log back in, and open the course.
  - Expected: The course resumes from the user's last completed step (or offers a "Continue"/"Resume" option leading there).
  - Bug Report:
    - Issue: Test blocked by the login failure (same root cause as FT-02)
    - Actual: Completed 3 of 5 Spanish lessons, logged out, and attempted to log back in with the registered credentials — login is always rejected with "Invalid email or password" and /dashboard redirects to /login. The resume behavior after re-login cannot be reached or verified.

- [X] FT-10: User can view a progress summary across lessons
  - Action: Complete one or more lessons/exercises/quizzes, then open the progress summary page/section.
  - Expected: A summary shows per-lesson/level progress (e.g., completed vs. total items, scores).

## Constraint
- [X] CS-01: Registration is blocked with empty required fields
  - Action: Submit the registration form leaving required fields (e.g., email or password) empty.
  - Expected: Submission is prevented and a validation error is shown; no account is created.

- [X] CS-02: Duplicate registration with an already-used email is rejected
  - Action: Register again with the same email used in FT-01.
  - Expected: An error such as "Email already in use" is shown and no second account is created.

- [X] CS-03: Locked lessons cannot be accessed before completing prior content
  - Action: On a fresh course, attempt to open a lesson/quiz that follows an incomplete lesson (e.g., Level 2 while Level 1 is unfinished).
  - Expected: The later item is locked/disabled or access is denied until the prior lesson is completed.

- [ ] CS-04: Quiz/lesson cannot be submitted with unanswered questions
  - Action: Leave one or more questions unanswered and click "Submit" on an exercise or quiz.
  - Expected: Submission is blocked with a message prompting completion of all questions.
  - Bug Report:
    - Issue: Missing validation feedback — blocking works but no prompt message is shown
    - Actual: With no option selected and empty text inputs, the "Check Answer" button is disabled and clicking it does nothing (submission is blocked), but no message prompting completion of the question(s) is displayed anywhere (no toast, tooltip, or inline hint).

- [ ] CS-05: Scores and progress persist after logout/login
  - Action: Complete items, log out, log back in, and check the progress summary.
  - Expected: Previously earned scores and completed lessons remain unchanged (not reset).
  - Bug Report:
    - Issue: Test blocked by the login failure (same root cause as FT-02)
    - Actual: Logged out after completing lessons; logging back in with the exact registered credentials always fails with "Invalid email or password" (verified on two separate accounts), so the progress summary after re-login cannot be reached to confirm persistence.

## Interaction
- [X] IX-01: Instant feedback is shown immediately after submitting an answer
  - Action: Submit an answer to an exercise question.
  - Expected: Correct/incorrect feedback (e.g., green checkmark / red X with the right answer) appears immediately.

- [X] IX-02: A score is displayed upon completing a quiz or exercise
  - Action: Finish and submit a quiz/exercise set.
  - Expected: A simple score/result (e.g., "8/10" or a percentage) is displayed to the user.

- [X] IX-03: Progress visual updates after completing an item
  - Action: Complete a lesson or quiz, then view the course overview or progress bar.
  - Expected: The progress indicator (bar/percentage/checkmark) updates to reflect the newly completed item.

## Content
- [X] CT-01: Lesson and question content matches the selected language
  - Action: Open a lesson in the chosen language (e.g., Spanish) and inspect its vocabulary and questions.
  - Expected: All displayed words/phrases/questions are in the selected target language and are relevant to language learning (not placeholder or unrelated text).

- [ ] CT-02: Progress summary shows correct data for each lesson/level
  - Action: Compare the progress summary with the lessons/quiz scores actually completed.
  - Expected: The summary accurately lists each lesson/level with its correct completion status and score values.
  - Bug Report:
    - Issue: Incorrect data — displayed per-lesson scores do not match the achieved results
    - Actual: Dashboard "Score" values contradict the actual results: a lesson finished 4/4 (100%) shows "Score: 125%", a lesson finished 3/4 (75%) shows "Score: 100%", and a lesson finished 2/4 (50%) shows "Score: 75%" (the value appears to be XP points mislabeled as a percentage). Completion counts/percentages (e.g., 1/3, 20%, 3 of 5 lessons) are correct.