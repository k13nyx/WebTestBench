# Test Result

## Functionality
- [X] FT-01: Register a new user account
  - Action: Enter a valid username, email, and password in the registration form and click "Register".
  - Expected: Account is created successfully and the user is redirected to the language selection page.
- [X] FT-02: Select a target language
  - Action: Click on a language card (e.g., "Spanish") from the available language options.
  - Expected: The chosen language is set as active and the course overview screen for that language is displayed.
- [X] FT-03: Start an initial lesson
  - Action: Click the "Start" button on Lesson 1 under Level 1.
  - Expected: The lesson player launches and displays the first exercise of Lesson 1.
- [X] FT-04: Answer a multiple-choice exercise
  - Action: Select an answer option in a multiple-choice question and click "Check".
  - Expected: The answer is submitted, evaluated immediately, and the option to proceed becomes active.
- [X] FT-05: Answer a text-input exercise
  - Action: Type the translation into the text input field in a fill-in-the-blank question and click "Check".
  - Expected: The typed response is evaluated and instant correctness feedback is displayed.
- [ ] FT-06: Complete a quiz and view score
  - Action: Answer the final question of a level quiz and click "Submit Quiz".
  - Expected: The quiz ends and a summary screen displays the user's final score and total correct answers.
  - Bug Report:
    - Issue: Missing Level Quiz and Submit Quiz Feature
    - Actual: Level quizzes do not exist in the curriculum (only standard lessons with a "Finish" button are present), and no "Submit Quiz" action or level quiz evaluation exists.
- [ ] FT-07: Resume an in-progress course
  - Action: Exit an ongoing lesson, return to the main dashboard, and click "Resume Course".
  - Expected: The application opens directly to the last uncompleted lesson or exercise the user was working on.
  - Bug Report:
    - Issue: Missing Course Resume Feature
    - Actual: There is no "Resume Course" button on the dashboard, and navigating back into an in-progress lesson resets the exercise index back to Question 1 instead of restoring the last uncompleted exercise.
- [X] FT-08: View lesson progress summary
  - Action: Navigate to the "Progress" dashboard.
  - Expected: Displays an overview showing completed lessons, current active level, and total completion percentage.

## Constraint
- [ ] CS-01: Prevent registration with empty fields
  - Action: Leave the registration fields blank and click "Register".
  - Expected: Registration is blocked, and validation error messages appear under all required fields.
  - Bug Report:
    - Issue: Missing Field-Level Validation Messages
    - Actual: While submission is blocked with a top-level toast error ("Please fill in all fields"), no inline validation error messages appear under any of the required input fields.
- [X] CS-02: Enforce sequential progression for locked lessons
  - Action: Click on an uncompleted, locked lesson (e.g., Lesson 3 while Lesson 1 is incomplete).
  - Expected: The lesson remains locked and cannot be started until previous prerequisites are completed.
- [X] CS-03: Block submission when no answer is provided
  - Action: Click "Check" on an exercise without selecting an option or entering any text.
  - Expected: Submission is prevented (button remains disabled or an alert prompts the user to provide an answer).

## Interaction
- [ ] IX-01: Display instant feedback for correct answer
  - Action: Select the correct answer option in an exercise and click "Check".
  - Expected: A green banner appears displaying "Correct!", plays a success chime, and reveals the "Continue" button.
  - Bug Report:
    - Issue: Missing Audio Chime Feedback
    - Actual: The green "Correct!" banner and "Continue" button appear as expected, but no success chime or audio feedback is played.
- [ ] IX-02: Display instant feedback for incorrect answer
  - Action: Select an incorrect answer option in an exercise and click "Check".
  - Expected: A red banner appears displaying "Incorrect" alongside the correct solution, and reveals the "Continue" button.
  - Bug Report:
    - Issue: Incorrect Banner Text and Missing Solution
    - Actual: The banner displays the text "Not quite right" instead of "Incorrect", and does not display the correct solution alongside the message in the banner.
- [X] IX-03: Dynamic lesson progress bar update
  - Action: Complete an exercise item within a lesson and click "Continue".
  - Expected: The top progress bar increments smoothly to reflect the updated fraction of completed exercises in the lesson.

## Content
- [ ] CT-01: Structured curriculum hierarchy display
  - Action: Open the course curriculum page.
  - Expected: Content is clearly grouped into distinct levels (e.g., Level 1, Level 2), each containing ordered sequences of lessons, exercises, and a concluding quiz.
  - Bug Report:
    - Issue: Missing Concluding Quiz in Curriculum Levels
    - Actual: Course levels contain ordered lesson sequences and exercises, but none of the levels contain a concluding quiz.
- [X] CT-02: Target language content alignment
  - Action: Inspect the vocabulary, question prompts, and options within the selected language course.
  - Expected: All lesson texts, exercise prompts, and answer choices match the selected target language without untranslated placeholders or broken strings.
