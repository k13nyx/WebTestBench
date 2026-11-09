# Test Checklist

*Preconditions: application is running and reachable; use the default languages/levels/lessons already present. A single new account created in FT-01 is reused for all subsequent items.*

## Functionality
- [ ] FT-01: Register a new learner account
  - Action: Click the "Register"/"Sign up" entry point, enter a new email, a password (and name/username if the form asks for one), and submit the form.
  - Expected: The account is created, the app switches to a signed-in state (account name/email visible in the header), and no error is shown.

- [ ] FT-02: Log in with an existing account
  - Action: Sign out if signed in, then use the "Log in"/"Sign in" form with the email and password from FT-01.
  - Expected: Login succeeds and the dashboard with the course list for that account is displayed.

- [ ] FT-03: Choose a language to learn
  - Action: Open the language list on the dashboard and select one language (e.g., Spanish).
  - Expected: The chosen language becomes the active one, its levels/lessons/exercises/quizzes are shown, and any previously selected language is no longer active.

- [ ] FT-04: Course content is organized by level in a fixed sequence
  - Action: Open the course outline of the active language and expand each level.
  - Expected: Levels (e.g., Beginner, Intermediate, Advanced) appear in increasing difficulty order, and each level lists its lessons, exercises and quizzes in one fixed order.

- [ ] FT-05: Start a course from the beginning
  - Action: In the course outline, click "Start" (or the first lesson/exercise) of the first level.
  - Expected: The first lesson/exercise of that level opens with its content visible and a way to continue through its items.

- [ ] FT-06: Resume an in-progress course where it was left off
  - Action: Complete part of a lesson, leave it (back navigation or page reload), then return to the course outline and use "Resume"/"Continue".
  - Expected: The app reopens the last incomplete lesson/exercise of the active language at the exact item where the user stopped; already completed items are not replayed.

- [ ] FT-07: Answer each type of question
  - Action: Work through a quiz/exercise containing multiple choice, fill-in-the-blank and matching items; select an option, type text, and pair the matches respectively.
  - Expected: Each item renders its own input control, accepts the user's input, and the answer is registered for that item.

- [ ] FT-08: Finishing an item records it as completed
  - Action: Answer the final question of a lesson/exercise and finish it.
  - Expected: The item shows a completed state (e.g., checkmark / "Completed") and is counted as completed in the progress summary.

- [ ] FT-09: A simple score is shown after a quiz
  - Action: Answer every question of a quiz and submit it.
  - Expected: A simple score (e.g., "8/10" or "80%") is displayed, and the number matches the count of answers graded correct.

- [ ] FT-10: View a progress summary across lessons
  - Action: Open the "Progress"/"My Progress" entry in the navigation.
  - Expected: A summary lists the lessons of the active language with their completion state (and per-level totals), including every lesson completed so far.

## Constraint
- [ ] CS-01: Registration rejects invalid input
  - Action: Submit the registration form with a blank required field, then with a malformed email, then with a mismatched password confirmation.
  - Expected: Each invalid submission is rejected with a clear inline error message next to the offending field, and no account is created.

- [ ] CS-02: A duplicate account cannot be registered
  - Action: Register again using the email address of the account created in FT-01.
  - Expected: Registration is refused with an "already registered/exists" message, and no second account is created.

- [ ] CS-03: Login with a wrong password is rejected
  - Action: On the login form, enter the registered email with an incorrect password and submit.
  - Expected: An error message is displayed and the dashboard/course content is not shown.

- [ ] CS-04: The lesson sequence is enforced
  - Action: On a course where the first lesson is not yet completed, attempt to open the second lesson/exercise/quiz of that level from the outline.
  - Expected: The later item stays locked (disabled or blocked with a "complete the previous item first" message) and its content does not open.

## Interaction
- [ ] IX-01: Instant feedback for a correct answer
  - Action: Answer a question correctly and submit.
  - Expected: Immediately, without leaving the item or reloading the page, a positive feedback message (e.g., "Correct!") and correct-answer styling appear.

- [ ] IX-02: Instant feedback for an incorrect answer
  - Action: Answer a question incorrectly and submit.
  - Expected: Immediately a "Incorrect"/"Try again" message appears, the chosen option is marked as wrong, and the correct answer is revealed.

- [ ] IX-03: Continue is gated until an answer is given
  - Action: Open a question and inspect the Continue/Next/Submit control before answering, then select an answer and inspect it again.
  - Expected: The control is disabled (or does nothing when clicked) until an answer is provided, and becomes enabled as soon as an answer is given.

## Content
- [ ] CT-01: Content matches the selected language and lesson topic
  - Action: Open a lesson, an exercise and a quiz in the active language and read the prompts, options and vocabulary.
  - Expected: All content is about the selected language (e.g., a Spanish lesson contains Spanish words/phrases with translations), and no content from another language appears.

- [ ] CT-02: Content is complete, with no placeholders
  - Action: Inspect question options, lesson instructions, feedback messages and button labels across several levels.
  - Expected: Every option, instruction and message has real meaningful text — no empty options and no "Lorem ipsum", "TODO", "undefined" or truncated sentences.

- [ ] CT-03: The summary shows the learner's real data
  - Action: Complete two lessons in the active language, then open the progress summary.
  - Expected: The summary lists exactly the lessons/levels actually completed with their real completion state and counts, and shows no placeholder or zero values for work already completed.