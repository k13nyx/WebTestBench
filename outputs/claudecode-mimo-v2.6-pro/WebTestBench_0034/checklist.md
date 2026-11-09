# Test Checklist

## Functionality
- [ ] FT-01: User can register a new account with valid credentials.
  - Action: Open the registration form, fill in all required fields (e.g., username, email, password) with valid values, and submit.
  - Expected: The account is created and the user is logged in / redirected to the language selection page.
- [ ] FT-02: User can pick a language to learn after registering.
  - Action: On the language selection screen, choose one of the offered languages and confirm the selection.
  - Expected: The selected language is saved to the user's profile and the course overview for that language is displayed.
- [ ] FT-03: User can start a course and see lessons organized by level.
  - Action: Open the selected language course and view the course structure.
  - Expected: Lessons, exercises, and quizzes are listed and grouped under levels (e.g., Level 1, Level 2) in a clear sequence.
- [ ] FT-04: User can start a lesson and open its first exercise or quiz item.
  - Action: Click "Start" (or the first uncompleted lesson) in the course.
  - Expected: The lesson launches and presents the first question/exercise item of that lesson.
- [ ] FT-05: User can resume a partially completed course at the last unfinished item.
  - Action: Complete part of a lesson, leave the course, then return and click "Resume" (or re-enter the course).
  - Expected: The application returns to the exact next uncompleted item rather than restarting from the beginning.
- [ ] FT-06: User can answer a multiple-choice question and submit the answer.
  - Action: In a multiple-choice exercise, select one option and submit.
  - Expected: The selected answer is accepted and evaluated; the interface moves to feedback for that item.
- [ ] FT-07: User can answer a text-entry question and submit the answer.
  - Action: In a free-text exercise, type an answer into the input field and submit.
  - Expected: The typed answer is accepted and evaluated; the interface moves to feedback for that item.
- [ ] FT-08: User can answer at least one additional question type provided by the course (e.g., matching or fill-in-the-blank).
  - Action: Navigate to an exercise of a question type other than multiple choice and text entry, complete it, and submit.
  - Expected: The interaction for that question type is completable and the answer is accepted and evaluated.
- [ ] FT-09: User receives instant feedback after submitting each answer.
  - Action: Submit an answer to any question and observe the screen before proceeding.
  - Expected: Immediate feedback is shown indicating whether the submitted answer is correct or incorrect (without requiring to finish the whole quiz).
- [ ] FT-10: A simple score is displayed for the answered items.
  - Action: Answer one correct and one incorrect item, then view the current score display.
  - Expected: A score reflecting the answers (e.g., number or percentage of correct answers) is shown and updates after each submission.
- [ ] FT-11: User can complete a lesson and proceed to the next lesson in sequence.
  - Action: Answer all items in a lesson and continue past the lesson end screen.
  - Expected: The lesson is marked complete and the next lesson in the level becomes available/openable.
- [ ] FT-12: User can view a summary of progress across lessons.
  - Action: Open the progress summary view (e.g., "My Progress" / dashboard).
  - Expected: A per-lesson overview is shown indicating completion status (e.g., completed / in progress / not started) and scores for the selected language.

## Constraint
- [ ] CS-01: Registration cannot be completed with missing required fields.
  - Action: Leave a required registration field (e.g., email or password) empty and submit the form.
  - Expected: The submission is rejected and a validation error identifies the missing field; no account is created.
- [ ] CS-02: Registration cannot be completed with an invalid email format.
  - Action: Enter an email without a valid format (e.g., "user@") and submit the registration form.
  - Expected: The submission is rejected with an email format error; no account is created.
- [ ] CS-03: An answer cannot be submitted without a selection or input.
  - Action: Click the submit/confirm button on a question without selecting an option or typing text.
  - Expected: The submission is blocked and a message prompts the user to provide an answer; no feedback or score change occurs.
- [ ] CS-04: A lesson cannot be opened before its preceding lesson in the sequence is completed.
  - Action: From the course overview, attempt to open a lesson whose prerequisite lesson is not completed.
  - Expected: Access is prevented (locked state) and the lesson cannot be started until the earlier lesson is completed.
- [ ] CS-05: A course cannot be started before a language is selected.
  - Action: As a newly registered user, attempt to access a course/lesson without choosing a language.
  - Expected: Access is prevented and the user is directed to the language selection screen.

## Interaction
- [ ] IX-01: Correct and incorrect answers are visually distinguishable in the feedback.
  - Action: Submit one correct answer and one incorrect answer and compare the feedback styling.
  - Expected: The two feedback states use clearly different visual cues (e.g., distinct color and indicator) so the user can tell right from wrong at a glance.
- [ ] IX-02: The answered item is locked after submission until the user moves on.
  - Action: Submit an answer to a question, then attempt to change the selection or resubmit a different answer for the same item.
  - Expected: The submitted answer cannot be altered and no new feedback/score is produced for that item; a control to proceed to the next item is available.

## Content
- [ ] CT-01: Course content matches the selected language.
  - Action: Pick a language and browse its lessons, exercises, and quiz questions.
  - Expected: All learning content (words, phrases, prompts, audio/text) is in/for the selected language, not another language.
- [ ] CT-02: Lesson, level, and quiz content reflects the stated language-learning theme.
  - Action: Review the text and labels shown across levels and lesson items.
  - Expected: Content is language-learning material (vocabulary, grammar, translation, etc.), with no irrelevant or placeholder content (e.g., "Lorem ipsum").