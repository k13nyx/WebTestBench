# Test Checklist

## Functionality
- [ ] FT-01: New user can register an account with valid details
  - Action: On the registration page, fill in all required fields (name, email, password) with valid values and click the "Register" / "Sign Up" button.
  - Expected: The account is created and the user is directed to the login page or the language selection / dashboard page.
- [ ] FT-02: Registered user can log in
  - Action: On the login page, enter the email and password used during registration and click the "Log In" / "Sign In" button.
  - Expected: The user is logged in and reaches the language selection page or personal dashboard.
- [ ] FT-03: User can pick a language to learn
  - Action: On the language selection page, click on any one of the offered language options (e.g., "Spanish").
  - Expected: The course for the selected language opens and its lessons are displayed.
- [ ] FT-04: Course shows a structured sequence organized by level
  - Action: Open a course and inspect its course page.
  - Expected: Lessons, exercises, and quizzes are grouped into ordered levels (e.g., Level 1, Level 2) and listed in a sequential order within each level.
- [ ] FT-05: User can start the first lesson of a course
  - Action: Click the first lesson of the selected course, then click "Start".
  - Expected: The lesson opens and its first content screen or question is shown.
- [ ] FT-06: User can answer different question types
  - Action: Work through a lesson containing at least two question types (e.g., multiple choice and fill-in-the-blank), select/enter an answer for each, and submit via the "Check"/"Submit" button.
  - Expected: Each answer is accepted and submitted, and the user can proceed to the next question.
- [ ] FT-07: A completed quiz shows a simple score
  - Action: Answer all questions in a default quiz to the end and submit the final answer.
  - Expected: A results screen displays a score (e.g., points or "X/Y correct" or percentage).
- [ ] FT-08: User can resume an in-progress course
  - Action: Partially complete a lesson, leave the course (navigate away or log out and back in), then reopen the same course and click the resume/continue control.
  - Expected: The user returns to the correct point — the same lesson and question where they left off, not back at the start.
- [ ] FT-09: User can view a progress summary
  - Action: After completing at least one lesson, navigate to the progress/dashboard/summary page.
  - Expected: A summary of progress across lessons is displayed (e.g., completed lessons, current lesson, overall completion percentage).

## Constraint
- [ ] CS-01: Registration is blocked with empty or invalid required fields
  - Action: On the registration page, submit the form with an empty required field, then again with an invalid email format (e.g., "abc@").
  - Expected: Registration is rejected both times with an error message, and no account is created.
- [ ] CS-02: Registration is blocked with an already-registered email
  - Action: Attempt to register a second time using the same email as FT-01 with a different password.
  - Expected: Registration is rejected with a message indicating the email is already in use.
- [ ] CS-03: Login is blocked with incorrect credentials
  - Action: On the login page, enter a registered email with a wrong password and click "Log In".
  - Expected: Login fails with an error message and the user is not granted access to the dashboard.
- [ ] CS-04: Lessons are inaccessible without logging in
  - Action: While logged out, attempt to open a course or lesson page directly (e.g., via a previously used link or navigation menu).
  - Expected: The lesson content is not shown; the user is redirected to the login/registration page.
- [ ] CS-05: Answer cannot be submitted without selecting or typing one
  - Action: On a question screen, click "Check"/"Submit" without choosing any option or entering any text.
  - Expected: The answer is not accepted — the submit action is disabled or an error/prompt asks the user to select an answer first.

## Interaction
- [ ] IX-01: Instant feedback appears after each answer
  - Action: Answer one question correctly and submit, then answer the next question incorrectly and submit.
  - Expected: Feedback appears immediately after each submission (e.g., green "Correct" / red "Incorrect" indication with the correct answer shown when wrong) without a page reload delay or manual refresh.
- [ ] IX-02: Success confirmation appears after registration
  - Action: Complete the registration form with valid details and submit.
  - Expected: A visible success confirmation is shown (e.g., toast or message such as "Account created successfully") before/while moving to the next page.
- [ ] IX-03: Progress indicator updates after lesson completion
  - Action: Note the progress indicator (bar, percentage, or checkmark count) before completing a lesson, then finish that lesson.
  - Expected: The progress display visibly updates immediately (e.g., the bar advances or the lesson gains a "completed" checkmark).

## Content
- [ ] CT-01: Offered languages are real, recognizable languages
  - Action: Inspect the list of language options on the language selection page.
  - Expected: Every option is a real-world language relevant to language learning (e.g., Spanish, French, Japanese), with correct names and no unrelated or placeholder entries.
- [ ] CT-02: Lesson and quiz content matches the selected language
  - Action: Open lessons and a quiz inside a chosen course (e.g., "Spanish") and examine the words, phrases, questions, and answer options.
  - Expected: All practice content is in the selected language (or translates into it) and is relevant to the lesson topic — no content from a different language or unrelated subject.
- [ ] CT-03: Progress summary data matches actual completed lessons
  - Action: Compare the numbers shown on the progress summary page (completed lessons count, current lesson, percentage) with the lessons actually completed and in progress during this test session.
  - Expected: Every figure shown in the summary accurately reflects the real completed and in-progress lessons, with no missing or inflated counts.