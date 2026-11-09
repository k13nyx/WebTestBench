# Test Checklist

## Functionality
- [ ] FT-01: Register a new account with valid details.
  - Action: Open the sign-up page, enter a name, unique email, and matching passwords, then click "Sign up".
  - Expected: Account is created, the user is logged in, and the language selection page loads.
- [ ] FT-02: Log in with an existing account.
  - Action: Log out, then log in with the registered email and password.
  - Expected: The dashboard loads and shows the user's name.
- [ ] FT-03: Start a course by picking a language.
  - Action: On the language selection page, click one available language card.
  - Expected: The course page opens and lists its levels in order (e.g., Beginner, Intermediate, Advanced).
- [ ] FT-04: View lessons, exercises, and quizzes organized under each level.
  - Action: Click the first level.
  - Expected: Numbered lessons appear in order, and each lesson lists its exercises, with a quiz at the end of the level.
- [ ] FT-05: Answer a multiple-choice question.
  - Action: Select one option, click "Submit", then click "Next".
  - Expected: The answer is accepted and the next question appears.
- [ ] FT-06: Answer a fill-in-the-blank question.
  - Action: Type the answer in the blank, click "Submit", then click "Next".
  - Expected: The typed answer is accepted and the next question appears.
- [ ] FT-07: Answer a matching or word-ordering question.
  - Action: Match the pairs or arrange the words in order, then click "Submit".
  - Expected: The answer is accepted and feedback is shown.
- [ ] FT-08: Complete a quiz and view the score.
  - Action: Answer every question in the Level 1 quiz and click "Finish".
  - Expected: A results screen shows the score as "X / Y" and a percentage matching the answers given.
- [ ] FT-09: Resume a partially completed course.
  - Action: Complete two lessons, log out, log in, and click "Continue" or "Resume course".
  - Expected: The course opens at the first incomplete lesson, and the two completed lessons still show as complete.
- [ ] FT-10: Open the progress summary.
  - Action: Click "Progress" in the navigation.
  - Expected: A summary page shows completed lessons, quiz scores by level, and overall completion.

## Constraint
- [ ] CS-01: Registration rejects a duplicate email.
  - Action: Register with an email that already has an account.
  - Expected: The error "Email already registered" appears, and no new account is created.
- [ ] CS-02: Registration validates required fields and formats.
  - Action: Submit the sign-up form with empty fields, an invalid email (e.g., "abc"), and mismatched passwords.
  - Expected: Each invalid field shows an inline error, and the form is not submitted.
- [ ] CS-03: Submitting without an answer is blocked.
  - Action: On any question, click "Submit" without selecting or entering an answer.
  - Expected: The question does not advance, the score does not change, and a message such as "Please select an answer" appears.
- [ ] CS-04: Locked levels cannot be opened.
  - Action: On a new course, click Level 2 before completing Level 1.
  - Expected: Level 2 is marked as locked, and its lessons and quiz do not open.
- [ ] CS-05: Lessons cannot be skipped within a level.
  - Action: On a new course, click Lesson 3 before completing Lessons 1 and 2.
  - Expected: Lesson 3 is marked as locked and does not open.

## Interaction
- [ ] IX-01: Correct answers show instant positive feedback.
  - Action: Submit a correct answer on any question.
  - Expected: The answer is highlighted green, a "Correct!" message appears immediately, and the running score increases.
- [ ] IX-02: Incorrect answers show instant negative feedback with the right answer.
  - Action: Submit a wrong answer on any question.
  - Expected: The chosen answer is highlighted red, a "Incorrect" message appears immediately, and the correct answer is displayed.
- [ ] IX-03: Progress indicator updates as questions are answered.
  - Action: Answer the first two questions of an exercise.
  - Expected: The indicator reads "Question 2 of N" (or equivalent), and the progress bar fills proportionally.

## Content
- [ ] CT-01: Lesson content matches the selected language.
  - Action: Open any lesson in the chosen course.
  - Expected: Prompts, vocabulary, and answer options are in the target language, with no unrelated language mixed in.
- [ ] CT-02: Progress summary figures match actual completion.
  - Action: Note the completed lessons and quiz scores on the course page, then open the progress summary.
  - Expected: The lesson count, quiz scores, and overall percentage on the summary match the course page exactly.