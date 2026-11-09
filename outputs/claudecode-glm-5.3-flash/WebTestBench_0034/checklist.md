# Test Checklist

## Functionality
- [ ] FT-01: New user can register an account
  - Action: Fill in the registration form (e.g., name, email, password) and click the "Sign Up" / "Register" button.
  - Expected: Registration succeeds and the user is logged in / taken to the main dashboard.
- [ ] FT-02: Registered user can log in with valid credentials
  - Action: Enter the credentials used in FT-01 and click "Log In".
  - Expected: User reaches their dashboard showing their available courses/progress.
- [ ] FT-03: User can pick a language from the language selection
  - Action: Open the language selection (e.g., a list of languages on the dashboard) and select one language (e.g., "Spanish").
  - Expected: The chosen language's course/level structure is displayed.
- [ ] FT-04: Course content is organized by level with lessons, exercises, and quizzes
  - Action: View the selected language's course overview.
  - Expected: Multiple levels are shown, each containing a sequence of lessons, exercises, and quizzes in order.
- [ ] FT-05: User can start a lesson and view its content
  - Action: Click the first available lesson in the sequence.
  - Expected: The lesson opens and displays its learning content (vocabulary, phrases, or grammar material).
- [ ] FT-06: User can complete an exercise with multiple-choice questions
  - Action: Answer a multiple-choice exercise by selecting an option and submitting.
  - Expected: The answer is accepted and recorded.
- [ ] FT-07: User can answer typed/fill-in-the-blank questions
  - Action: Type an answer into a text input for a translation or fill-in-the-blank exercise and submit.
  - Expected: The typed answer is accepted and evaluated.
- [ ] FT-08: User can complete a quiz at the end of a level
  - Action: Answer all questions in a quiz and submit it.
  - Expected: The quiz finishes and a score/result is shown.
- [ ] FT-09: User can resume a course at the last unfinished item
  - Action: Complete part of a course, log out, log back in, and open the course.
  - Expected: The course resumes from the user's last completed step (or offers a "Continue"/"Resume" option leading there).
- [ ] FT-10: User can view a progress summary across lessons
  - Action: Complete one or more lessons/exercises/quizzes, then open the progress summary page/section.
  - Expected: A summary shows per-lesson/level progress (e.g., completed vs. total items, scores).

## Constraint
- [ ] CS-01: Registration is blocked with empty required fields
  - Action: Submit the registration form leaving required fields (e.g., email or password) empty.
  - Expected: Submission is prevented and a validation error is shown; no account is created.
- [ ] CS-02: Duplicate registration with an already-used email is rejected
  - Action: Register again with the same email used in FT-01.
  - Expected: An error such as "Email already in use" is shown and no second account is created.
- [ ] CS-03: Locked lessons cannot be accessed before completing prior content
  - Action: On a fresh course, attempt to open a lesson/quiz that follows an incomplete lesson (e.g., Level 2 while Level 1 is unfinished).
  - Expected: The later item is locked/disabled or access is denied until the prior lesson is completed.
- [ ] CS-04: Quiz/lesson cannot be submitted with unanswered questions
  - Action: Leave one or more questions unanswered and click "Submit" on an exercise or quiz.
  - Expected: Submission is blocked with a message prompting completion of all questions.
- [ ] CS-05: Scores and progress persist after logout/login
  - Action: Complete items, log out, log back in, and check the progress summary.
  - Expected: Previously earned scores and completed lessons remain unchanged (not reset).

## Interaction
- [ ] IX-01: Instant feedback is shown immediately after submitting an answer
  - Action: Submit an answer to an exercise question.
  - Expected: Correct/incorrect feedback (e.g., green checkmark / red X with the right answer) appears immediately.
- [ ] IX-02: A score is displayed upon completing a quiz or exercise
  - Action: Finish and submit a quiz/exercise set.
  - Expected: A simple score/result (e.g., "8/10" or a percentage) is displayed to the user.
- [ ] IX-03: Progress visual updates after completing an item
  - Action: Complete a lesson or quiz, then view the course overview or progress bar.
  - Expected: The progress indicator (bar/percentage/checkmark) updates to reflect the newly completed item.

## Content
- [ ] CT-01: Lesson and question content matches the selected language
  - Action: Open a lesson in the chosen language (e.g., Spanish) and inspect its vocabulary and questions.
  - Expected: All displayed words/phrases/questions are in the selected target language and are relevant to language learning (not placeholder or unrelated text).
- [ ] CT-02: Progress summary shows correct data for each lesson/level
  - Action: Compare the progress summary with the lessons/quiz scores actually completed.
  - Expected: The summary accurately lists each lesson/level with its correct completion status and score values.