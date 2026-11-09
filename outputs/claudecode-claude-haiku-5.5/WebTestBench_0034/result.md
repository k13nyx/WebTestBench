# Test Result

## Functionality
- [ ] FT-01: Register a new account with valid details.
  - Action: Open the sign-up page, enter a name, unique email, and matching passwords, then click "Sign up".
  - Expected: Account is created, the user is logged in, and the language selection page loads.
  - Result: PASS. Account created, "Account created! Let's pick your language." shown, and the URL is /select-language. The form has one password field only, so "matching passwords" could not be exercised.

- [ ] FT-02: Log in with an existing account.
  - Action: Log out, then log in with the registered email and password.
  - Expected: The dashboard loads and shows the user's name.
  - Bug Report:
    - Issue: Authentication Failure (login rejects just-registered credentials)
    - Actual: After logout, logging in with qa.tester.2026a@example.com / the registered password shows "Invalid email or password" twice. The page stays on /login and the dashboard never loads.

- [X] FT-03: Start a course by picking a language.
  - Action: On the language selection page, click one available language card.
  - Expected: The course page opens and lists its levels in order (e.g., Beginner, Intermediate, Advanced).
  - Result: PASS, with a note. Clicking the Spanish card selects it, and the course opens after clicking "Continue". The dashboard lists "1 Beginner" then "2 Elementary" in order.

- [ ] FT-04: View lessons, exercises, and quizzes organized under each level.
  - Action: Click the first level.
  - Expected: Numbered lessons appear in order, and each lesson lists its exercises, with a quiz at the end of the level.
  - Bug Report:
    - Issue: Missing Level Quiz / Incomplete Lesson Structure
    - Actual: Clicking the "Beginner" heading does nothing. Beginner lists three lessons (Greetings, Numbers 1-10, Colors) with no numbering. Each shows only a "4 questions" count, not its exercises. No quiz element or quiz text exists anywhere on the page (DOM search returned no "quiz" text or link).

- [X] FT-05: Answer a multiple-choice question.
  - Action: Select one option, click "Submit", then click "Next".
  - Expected: The answer is accepted and the next question appears.
  - Result: PASS, with a note. The button is labeled "Check Answer" and the advance button "Continue", not "Submit"/"Next". Selecting "Hola" and checking it showed "Correct!", and clicking Continue showed "Question 2 of 4" with a new question.

- [X] FT-06: Answer a fill-in-the-blank question.
  - Action: Type the answer in the blank, click "Submit", then click "Next".
  - Expected: The typed answer is accepted and the next question appears.
  - Result: PASS, with the same label note. The translation "Buenos días" for "Good morning" showed "Correct!", and Continue advanced to a "Fill in the Blank" question.

- [ ] FT-07: Answer a matching or word-ordering question.
  - Action: Match the pairs or arrange the words in order, then click "Submit".
  - Expected: The answer is accepted and feedback is shown.
  - Bug Report:
    - Issue: Required Question Type Not Available
    - Actual: The Greetings lesson (MC, translation, fill-in-blank, MC) and the Numbers 1-10 lesson (MC, translation, fill-in-blank, MC) contain no matching or word-ordering question. The Elementary lessons were locked, so they could not be checked.

- [ ] FT-08: Complete a quiz and view the score.
  - Action: Answer every question in the Level 1 quiz and click "Finish".
  - Expected: A results screen shows the score as "X / Y" and a percentage matching the answers given.
  - Bug Report:
    - Issue: Missing Quiz
    - Actual: No Level 1 quiz exists. The only results screens are per-lesson "Lesson Complete!" screens ("75%, You got 3 out of 4 correct"), and no "X / Y" quiz score is shown.

- [ ] FT-09: Resume a partially completed course.
  - Action: Complete two lessons, log out, log in, and click "Continue" or "Resume course".
  - Expected: The course opens at the first incomplete lesson, and the two completed lessons still show as complete.
  - Bug Report:
    - Issue: Authentication Failure (blocks resume)
    - Actual: Both lessons were completed (Greetings and Numbers 1-10; the dashboard shows "2 of 5 lessons", 40%). After logout, login fails with "Invalid email or password" (see FT-02), so the resume flow could not be reached. The dashboard has no "Continue"/"Resume course" button.

- [ ] FT-10: Open the progress summary.
  - Action: Click "Progress" in the navigation.
  - Expected: A summary page shows completed lessons, quiz scores by level, and overall completion.
  - Bug Report:
    - Issue: Missing Navigation Item
    - Actual: The logged-in header contains only a streak badge, an XP badge, and two unlabeled icon buttons. No "Progress" link or button exists in the navigation (verified on a fresh account's dashboard, and no link text matches "Progress"). No summary page was reached.

## Constraint
- [ ] CS-01: Registration rejects a duplicate email.
  - Action: Register with an email that already has an account.
  - Expected: The error "Email already registered" appears, and no new account is created.
  - Bug Report:
    - Issue: Incorrect Error Message
    - Actual: Submitting a duplicate email shows "An account with this email already exists", not "Email already registered". The user stays on /register, which suggests no account was created, but the account count was not verifiable from the UI.

- [ ] CS-02: Registration validates required fields and formats.
  - Action: Submit the sign-up form with empty fields, an invalid email (e.g., "abc"), and mismatched passwords.
  - Expected: Each invalid field shows an inline error, and the form is not submitted.
  - Bug Report:
    - Issue: Missing Inline Validation
    - Actual: With name and password empty and email "abc", clicking "Create Account" keeps the user on /register, but no inline error text appears for any field. The form has no confirm-password field, so mismatched passwords could not be tested.

- [ ] CS-03: Submitting without an answer is blocked.
  - Action: On any question, click "Submit" without selecting or entering an answer.
  - Expected: The question does not advance, the score does not change, and a message such as "Please select an answer" appears.
  - Bug Report:
    - Issue: Missing Validation Message
    - Actual: The "Check Answer" button is disabled until an answer is chosen, so the question does not advance. However, no message such as "Please select an answer" appears in the DOM at any point.

- [X] CS-04: Locked levels cannot be opened.
  - Action: On a new course, click Level 2 before completing Level 1.
  - Expected: Level 2 is marked as locked, and its lessons and quiz do not open.
  - Result: PASS, with a note. On a fresh course, clicking "Family Members" under Elementary did not navigate, and the URL stayed /dashboard. The lock is shown only by lucide lock icons, with no "locked" text or aria-label.

- [X] CS-05: Lessons cannot be skipped within a level.
  - Action: On a new course, click Lesson 3 before completing Lessons 1 and 2.
  - Expected: Lesson 3 is marked as locked and does not open.
  - Result: PASS, with a note. On a fresh course, clicking "Colors" (lesson 3) did not navigate, and the URL stayed /dashboard. The lock is shown only by an icon, with no text.

## Interaction
- [ ] IX-01: Correct answers show instant positive feedback.
  - Action: Submit a correct answer on any question.
  - Expected: The answer is highlighted green, a "Correct!" message appears immediately, and the running score increases.
  - Bug Report:
    - Issue: No Running Score Displayed
    - Actual: "Correct!" appears immediately and the correct option gets a check icon. No running score is shown during the exercise, and the header XP stayed at 0 until the lesson finished. The green highlight is not verifiable from the DOM (no color attribute exposed).

- [ ] IX-02: Incorrect answers show instant negative feedback with the right answer.
  - Action: Submit a wrong answer on any question.
  - Expected: The chosen answer is highlighted red, a "Incorrect" message appears immediately, and the correct answer is displayed.
  - Bug Report:
    - Issue: Incorrect Feedback Text
    - Actual: For a wrong answer, the message reads "Not quite right", not "Incorrect". The correct answer is displayed ("Correct answer: noches" and "Correct answer: Three"), but the chosen-answer red highlight is not verifiable from the DOM. Note: in the Numbers lesson, I typed "tres" for the prompt "Translate the number: 'Tres'". The expected answer is "Three", so that result was a wrong answer by my input, and the app handled it correctly.

- [ ] IX-03: Progress indicator updates as questions are answered.
  - Action: Answer the first two questions of an exercise.
  - Expected: The indicator reads "Question 2 of N" (or equivalent), and the progress bar fills proportionally.
  - Bug Report:
    - Issue: Progress Bar Not Verifiable / Indicator Off-by-One
    - Actual: After answering two questions the indicator reads "Question 3 of 4" (current question, not answered count). The progress bar's `progressbar` element exposes no aria-valuenow, so proportional fill could not be verified from the DOM.

## Content
- [X] CT-01: Lesson content matches the selected language.
  - Action: Open any lesson in the chosen course.
  - Expected: Prompts, vocabulary, and answer options are in the target language, with no unrelated language mixed in.
  - Result: PASS, with a note. Answer options and vocabulary are Spanish (Hola, Adiós, Gracias, Cinco, Seis, Siete, noches, tres). English appears only in instructions and glosses, such as "How do you say 'Hello' in Spanish?".

- [ ] CT-02: Progress summary figures match actual completion.
  - Action: Note the completed lessons and quiz scores on the course page, then open the progress summary.
  - Expected: The lesson count, quiz scores, and overall percentage on the summary match the course page exactly.
  - Bug Report:
    - Issue: Score Data Mismatch / Progress Summary Unreachable
    - Actual: The course page shows "Score: 100%" for both Greetings and Numbers 1-10. Each lesson's completion screen reported 75% (3 of 4 correct), so the course page disagrees with the lesson results. The progress summary (FT-10) could not be opened, so the summary side of the comparison was not checked. The course page's "40%, 2 of 5 lessons" is consistent with the lesson count.